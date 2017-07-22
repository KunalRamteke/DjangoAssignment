# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-10 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=70)),
                ('MobileNo', models.CharField(max_length=10)),
            ],
        ),
    ]