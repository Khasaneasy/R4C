# Generated by Django 3.2.3 on 2024-12-19 09:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]