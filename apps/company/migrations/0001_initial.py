# Generated by Django 4.2.5 on 2023-11-03 05:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='company/images')),
            ],
            options={'verbose_name_plural': 'About'},
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('open_week', models.CharField(max_length=50)),
                ('close_week', models.CharField(max_length=50)),
                ('open_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=100)),
            ],
            options={'verbose_name_plural': 'Phone'},
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='company/images')),
                ('picture', models.ImageField(upload_to='company/images')),
                ('qr_code', models.ImageField(upload_to='company/images')),
                ('qr_text', models.CharField(max_length=250)),
                ('bot_url', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=100)),
                ('delivery_price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Settings',
            }
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
            ],
            options={'verbose_name_plural': 'Social'},
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
