# Generated by Django 4.2.4 on 2023-09-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_guestmodel_is_staff_guestmodel_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
