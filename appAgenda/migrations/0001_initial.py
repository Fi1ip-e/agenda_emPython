# Generated by Django 4.2.6 on 2023-10-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('contato', models.CharField(max_length=100, verbose_name='Contato')),
            ],
        ),
    ]
