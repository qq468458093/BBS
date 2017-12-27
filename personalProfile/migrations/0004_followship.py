# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bbs', '0009_auto_20171201_2140'),
        ('personalProfile', '0003_delete_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='bbs.UserProfile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='bbs.UserProfile')),
            ],
        ),
    ]
