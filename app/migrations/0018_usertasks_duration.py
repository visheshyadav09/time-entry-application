# Generated by Django 3.1.7 on 2021-04-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_usertasks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertasks',
            name='duration',
            field=models.TimeField(default=None),
        ),
    ]
