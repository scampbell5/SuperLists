# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20151221_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
    ]
