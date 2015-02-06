# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlankPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Blank Page',
                'verbose_name_plural': 'Blank Pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': 'Course Page',
                'verbose_name_plural': 'Course Pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='TalkPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': 'Talk Page',
                'verbose_name_plural': 'Talk Pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='course',
            name='page',
            field=models.ForeignKey(to='extra_pages.CoursePage'),
            preserve_default=True,
        ),
    ]
