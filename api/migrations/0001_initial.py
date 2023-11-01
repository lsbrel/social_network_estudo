# Generated by Django 4.2.6 on 2023-11-01 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
                ('senha', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=16)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('conteudo', models.TextField(max_length=200)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('deleted_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
    ]
