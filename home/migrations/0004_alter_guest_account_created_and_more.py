# Generated by Django 4.2.4 on 2023-09-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_guest_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='account_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
