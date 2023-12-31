# Generated by Django 4.2.4 on 2023-08-31 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('curso', models.CharField(default='CST em Análise e Desenvolvimento de Sistemas', max_length=200)),
                ('media_curso', models.DecimalField(decimal_places=2, max_digits=3)),
                ('foto', models.ImageField(default='', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
