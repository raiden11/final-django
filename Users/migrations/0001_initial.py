# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-02 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNo', models.CharField(max_length=300, unique=True)),
                ('FirstName', models.CharField(max_length=300)),
                ('LastName', models.CharField(max_length=300)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('DisplayURL', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
