from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_ckeditor_5.fields import CKEditor5Field


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="Департамент")
    phones = models.TextField(blank=True, null=True, help_text="Телефони", verbose_name="Телефон")
    emails = models.TextField(blank=True, null=True, help_text="Электронні адреси", verbose_name="E-mail")
    manager = models.TextField(blank=True, null=True, verbose_name="Керівник")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменти"


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва компанії")
    legal_name = models.CharField(max_length=200, verbose_name="Юридична назва")
    edrpou = models.TextField(verbose_name="ЕДРПОУ")
    physical_address = models.TextField(blank=True, verbose_name="Фізична адреса")
    legal_address = models.TextField(verbose_name="Юридична адреса")
    account = models.TextField(verbose_name="Розрахунковий рахунок")
    tax_number = models.TextField(verbose_name="ІПН")
    single_tax_payer_certificate = models.TextField(verbose_name="Свідоцтво платника єдиного податку, №")
    phones = models.TextField(blank=True, null=True, help_text="Телефони", verbose_name="Телефон")
    emails = models.TextField(blank=True, null=True, help_text="Электронні адреси", verbose_name="E-mail")
    director =  models.TextField(blank=True, verbose_name="Директор")
    logo_image = models.ImageField(null=True, upload_to='images/', verbose_name="Логотип")
    favicon = models.ImageField(null=True, upload_to='images/', verbose_name="favicon")

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Компанія"
        verbose_name_plural = "Компанії"


class Worker(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    second_name = models.CharField(max_length=100, verbose_name="Фамілія")
    department = models.TextField()
    phone_number = models.TextField(null=True, verbose_name="Телефон")
    email = models.TextField(null=True, verbose_name="E-mail")
    photo_image = models.ImageField(blank=True, null=True, upload_to='images/', verbose_name="Фотографія")

    def __str__(self):
        return f"{self.name} {self.second_name}"

    class Meta:
        verbose_name='Співробітник компанії'
        verbose_name_plural = 'Співробітники компанії'


class History(models.Model):
    description=CKEditor5Field('Історія компанії', config_name='extends')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name='Історія компанії'
        verbose_name_plural = 'Історія компанії'


class Mission(models.Model):
    description=CKEditor5Field('Міссія компанії', config_name='extends')

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name='Міссія компанії'
        verbose_name_plural = 'Міссія компанії'
