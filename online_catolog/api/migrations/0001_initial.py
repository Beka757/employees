# Generated by Django 4.0.6 on 2022-07-12 10:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('employment_date', models.DateField(verbose_name='Дата приема на работу')),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(100000)], verbose_name='Заработная плата')),
                ('chief', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='api.employee', verbose_name='Начальник')),
            ],
        ),
    ]
