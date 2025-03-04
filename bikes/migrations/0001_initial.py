# Generated by Django 5.0.6 on 2024-05-21 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sizetype', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'size',
            },
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bikemodel', models.CharField(default='no bike model yet', max_length=255)),
                ('image', models.ImageField(default='default_img/', upload_to='bike_img/')),
                ('price', models.IntegerField()),
                ('miqdori', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bikes.category')),
                ('bikecolor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.colors')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bikes.size')),
            ],
            options={
                'db_table': 'bike',
            },
        ),
    ]
