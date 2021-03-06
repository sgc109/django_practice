# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-28 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180528_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-modify_date',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', help_text='one word for title alias.', unique=True, verbose_name='SLUG'),
        ),
    ]
