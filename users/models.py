from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, help_text='Введите вашу почту')
    avatar = models.ImageField(upload_to='users/photo', blank=True, null=True)
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона', help_text='Введите номер телефона')
    country = models.CharField(max_length=20, verbose_name='Страна проживания', help_text='Введите страну')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['username',]

    def __str__(self):
         return self.email

