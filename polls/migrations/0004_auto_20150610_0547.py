# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20150609_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
