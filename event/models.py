from django.db import models


class Player(models.Model):
    nickname = models.CharField(verbose_name='Никнейм', max_length=60)
    position = models.CharField(verbose_name='Позиция', max_length=10, blank=True)
    identity = models.CharField(verbose_name='Идентификатор', max_length=20, blank=True)
    clan = models.CharField(verbose_name='Клан', max_length=20, blank=True)

