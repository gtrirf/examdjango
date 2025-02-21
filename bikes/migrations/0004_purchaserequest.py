# Generated by Django 5.0.6 on 2024-05-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_alter_review_star_given'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'purchase_request',
            },
        ),
    ]
