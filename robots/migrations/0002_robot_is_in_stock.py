# Generated by Django 3.2.3 on 2024-12-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='is_in_stock',
            field=models.BooleanField(default=False),
        ),
    ]
