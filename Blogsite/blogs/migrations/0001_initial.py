# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_Name', models.CharField(max_length=50)),
                ('Comment', models.TextField()),
                ('Like', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Blog_Title', models.CharField(max_length=200)),
                ('Blog_Field', models.CharField(max_length=100)),
                ('URL', models.URLField()),
                ('Blog_Description', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='action',
            name='Blog_Title',
            field=models.ForeignKey(to='blogs.Blog'),
            preserve_default=True,
        ),
    ]
