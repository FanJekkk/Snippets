# Generated by Django 3.1 on 2022-09-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20220913_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='hidden',
            field=models.BooleanField(),
        ),
    ]