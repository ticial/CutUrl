from django.forms import ValidationError
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .models import Link
from .serializers import LinkSerializer


# В документации djoser'а есть другой способ изменить данные пользователя, 
# но там нужно менять каждое поле отдельными вызовами.
# Да и, как я понимаю, менять данные, которые используются при авторизации
# в нормальных проектах лучше вообще не позволять пользователям.
# Поэтому меняем руками и отправляем ошибки сами.
class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, req, *args, **kwargs):
        try:
            req.user.username = req.data['username']
            req.user.email = req.data['email']
            req.user.full_clean()
            req.user.save()
            return Response({'result': 'user updated'})
        except ValidationError as e:
            return Response(e.message_dict, status=400, exception=True)
                

class LinkView(APIView):
    permission_classes = [IsAuthenticated]

    # Создаем объект ссылки в базе данных
    def post(self, req):
        print('LinkView.post', req.data)

        try:
            req.data['user'] = req.user.id
            link = LinkSerializer(data=req.data)
            link.is_valid(raise_exception=True)
            link.save()
            return Response({'result': 'link created'})
        except ValidationError as e:
            return Response(e.message_dict, status=400, exception=True)
    
    # Удаляем ссылку по slug
    def delete(self, req, *args, **kwargs):
        print('LinkView.delete', req.data, kwargs)
        link = Link.objects.filter(pseudo_link=kwargs['slug']).first()
        if link:
            link.delete()
            return Response({'result': 'link deleted'})
        return Response({'result': 'link not found'}, status=400, exception=True)


class GetUserLinks(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LinkSerializer

    def get_queryset(self):
        return Link.objects.filter(user=self.request.user).order_by('-id') # Сортируем по убыванию, чтобы сверху были самые новые
            

# перенаправляем наши ссылки и считаем переходы
def redirect_and_count(req, slug):
    link = Link.objects.filter(pseudo_link=slug).first()
    if link:
        link.redirect_count += 1
        link.save()
        return redirect(link.original_link)
    return redirect(settings.CORS_ALLOWED_ORIGINS[0] + '/404')