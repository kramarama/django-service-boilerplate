# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-04 15:13
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
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
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('version', models.IntegerField(default=1, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('phones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, help_text='Номера телефонов вводятся в произвольном формате через запятую: четыре (4), шесть (6) или семь (7) цифр каждый', size=None, verbose_name='Номера телефонов служб')),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, default=list, help_text='E-mail адреса вводятся через запятую', size=None, verbose_name='E-mail адреса')),
                ('_contacts_index', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), blank=True, default=list, editable=False, size=None)),
            ],
            options={
                'verbose_name': 'контакт службы',
                'verbose_name_plural': 'контакты служб',
                'ordering': ['_contacts_index'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalContacts',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='Updated')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('version', models.IntegerField(default=1, editable=False)),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('phones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=list, help_text='Номера телефонов вводятся в произвольном формате через запятую: четыре (4), шесть (6) или семь (7) цифр каждый', size=None, verbose_name='Номера телефонов служб')),
                ('emails', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, default=list, help_text='E-mail адреса вводятся через запятую', size=None, verbose_name='E-mail адреса')),
                ('_contacts_index', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), blank=True, default=list, editable=False, size=None)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Создан'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical контакт службы',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
    ]