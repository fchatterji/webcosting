# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcosting', '0005_auto_20160507_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='degreintegration',
            name='fiab',
            field=models.DecimalField(blank=True, choices=[(0.75, 'tr\xe8s bas: 0.75')], decimal_places=3, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='degreintegration',
            name='degre_integration',
            field=models.CharField(choices=[('tr\xe8s bas', 'tr\xe8s bas'), ('bas', 'bas'), ('moyen', 'moyen'), ('\xe9lev\xe9', '\xe9lev\xe9'), ('tr\xe8s \xe9lev\xe9', 'tr\xe8s \xe9lev\xe9'), ('tr\xe8s tr\xe8s \xe9lev\xe9', 'tr\xe8s tr\xe8s \xe9lev\xe9')], default='moyen', max_length=100, verbose_name="degr\xe9 d'int\xe9gration"),
        ),
    ]