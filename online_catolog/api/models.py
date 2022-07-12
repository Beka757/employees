from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    position = models.CharField(max_length=50, verbose_name='Должность')
    employment_date = models.DateField(verbose_name='Дата приема на работу')
    salary = models.IntegerField(
        validators=[MinValueValidator(10000), MaxValueValidator(100000)],
        verbose_name='Заработная плата'
    )
    chief = models.ForeignKey(
        'api.Employee', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='employee', verbose_name='Начальник'
    )
