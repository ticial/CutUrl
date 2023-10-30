from django.urls import include, path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/links', views.GetUserLinks, basename='Link')

urlpatterns = [
    path('api/user-update', views.UpdateUser.as_view()),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/link-create', views.LinkView.as_view()),
    path('api/link-remove/<slug:slug>', views.LinkView.as_view()),
    path('$<slug>', views.redirect_and_count),
    
]
urlpatterns += router.urls