# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-12 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail_mvc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelOne',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_mvc.models.WagtailMvcMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='TestModelTwo',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_mvc.models.WagtailMvcMixin, 'wagtailcore.page'),
        ),
    ]
