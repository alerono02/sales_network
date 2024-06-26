# Generated by Django 4.2.7 on 2024-05-03 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название продукта')),
                ('model', models.CharField(max_length=200, verbose_name='Модель продукта')),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
