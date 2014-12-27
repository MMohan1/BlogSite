# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Like', models.IntegerField(default=0)),
                ('Blog_Title', models.ForeignKey(to='blogs.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Blog_Field',
            field=models.CharField(max_length=100, choices=[(b'Genral', b'Genral'), (b'Science', b'Science'), (b'IT Scotor', b'IT Scotor'), (b'History', b'History'), (b'New Teachnology', b'New Teachnology')]),
            preserve_default=True,
        ),
    ]
