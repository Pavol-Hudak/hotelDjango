# Generated by Django 4.2.4 on 2023-09-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_guestmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestmodel',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]