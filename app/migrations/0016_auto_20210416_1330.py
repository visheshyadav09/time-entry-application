# Generated by Django 3.1.7 on 2021-04-16 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210416_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertasks',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.userproject'),
        ),
    ]
