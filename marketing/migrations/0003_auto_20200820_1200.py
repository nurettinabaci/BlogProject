# Generated by Django 3.1 on 2020-08-20 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20200817_2356'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signup',
            new_name='Subscriber',
        ),
    ]
