# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0002_auto_20161106_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='drink',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='have_childern',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='methodology',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='smoke',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=80, null=True),
        ),
    ]
