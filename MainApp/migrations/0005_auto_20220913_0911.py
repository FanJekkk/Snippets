# Generated by Django 3.1 on 2022-09-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20220913_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='hidden',
            field=models.BooleanField(choices=[('0', 'Показывать'), ('1', 'Скрыть')]),
        ),
    ]