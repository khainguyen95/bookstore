# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('thumbnail', models.CharField(max_length=2083, null=True)),
                ('description', models.TextField(null=True)),
                ('author', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('no', models.CharField(max_length=100)),
                ('is_payment', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookine.Book')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('delivery', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=254)),
                ('sdt', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('manager', models.IntegerField(default=0)),
                ('book', models.ManyToManyField(through='bookine.Cart', to='bookine.Book')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookine.User'),
        ),
    ]
