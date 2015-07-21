# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='phone_no',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
