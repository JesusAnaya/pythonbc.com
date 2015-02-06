# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('where', models.CharField(max_length=255)),
                ('gmap', models.TextField()),
                ('external_url', models.URLField(null=True, blank=True)),
            ],
            options={
                'ordering': ('start',),
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('pages.page', models.Model),
        ),
    ]
