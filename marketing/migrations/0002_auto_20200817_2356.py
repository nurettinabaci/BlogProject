# Generated by Django 3.1 on 2020-08-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='confirmation_num',
            field=models.CharField(default=123456, max_length=15),
        ),
        migrations.AddField(
            model_name='signup',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
