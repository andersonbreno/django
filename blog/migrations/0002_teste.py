# Generated by Django 3.2.16 on 2022-10-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'ativo'), ('draft', 'Rascunho')], max_length=15)),
            ],
        ),
    ]
