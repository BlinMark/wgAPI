# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=60, verbose_name='Никнейм')),
                ('position', models.CharField(blank=True, max_length=10, verbose_name='Позиция')),
                ('identity', models.CharField(blank=True, max_length=20, verbose_name='Идентификатор')),
                ('clan', models.CharField(blank=True, max_length=20, verbose_name='Клан')),
            ],
        ),
    ]
