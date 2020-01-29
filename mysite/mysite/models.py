# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = [
    ['male', "Мужской"],
    ['female', "Женский"],
]

REL_CHOICES = [
    ['none', "Не определенно"],
    ['single', "Холост"],
    ['in_a_rel', "В отношениях"],
    ['engaged', "Помолвлен(а)"],
    ['married', "Женат/Замужем"],
    ['in_love', "Влюблен(а)"],
    ['complicated', "Все сложно"],
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    avatar = models.FileField(verbose_name="Аватар", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, verbose_name="Пол", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name="Статус отношений", choices=REL_CHOICES, default="none")

