# Generated by Django 4.1.1 on 2022-09-14 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('lang', models.CharField(choices=[('Python', 'Python'), ('Javascript', 'JavaScript'), ('C++', 'C++')], max_length=30)),
                ('code', models.TextField(default='', max_length=5000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('parametr', models.CharField(choices=[('Публичный', 'Публичный'), ('Частный', 'Частный')], max_length=30)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=5000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MainApp.snippet')),
            ],
        ),
    ]
