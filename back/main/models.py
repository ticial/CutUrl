from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    original_link = models.URLField('Оригинал')
    pseudo_link = models.SlugField('Псевдоним', unique=True)
    redirect_count = models.IntegerField('Число переходов', default=0)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'