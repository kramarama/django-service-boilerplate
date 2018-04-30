# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-08 11:45
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSubscribe',
            fields=[
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Создан')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='Updated')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('version', models.IntegerField(default=1, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Webhook')])),
                ('settings', django.contrib.postgres.fields.jsonb.JSONField()),
                ('events', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Подписка',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('version', models.IntegerField(default=1, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Webhook')])),
                ('settings', django.contrib.postgres.fields.jsonb.JSONField()),
                ('events', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='subscribes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
            },
        ),
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set([('name', 'type')]),
        ),
    ]