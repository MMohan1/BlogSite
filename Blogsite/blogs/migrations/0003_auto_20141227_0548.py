# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20141227_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='Blog_Title',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='blog',
            name='Like',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
