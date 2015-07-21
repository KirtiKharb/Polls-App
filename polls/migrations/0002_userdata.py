# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('phone_no', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
