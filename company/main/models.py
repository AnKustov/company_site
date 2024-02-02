from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from autoslug import AutoSlugField
from django_ckeditor_5.fields import CKEditor5Field
import random


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок посту")
    content=CKEditor5Field('Зміст посту', config_name='extends')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикації")
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True, verbose_name="Фотографія")
    photos = models.ManyToManyField('Photo', related_name='photo', verbose_name="Фотографії"),

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'



class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)  
    description=CKEditor5Field('Описание', config_name='extends')
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Зображення")
    slug = AutoSlugField(populate_from='name', unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категорія'
        verbose_name_plural = 'Категорії'


class Solution(models.Model):
    name = models.CharField(max_length=150, unique=True)  
    description=CKEditor5Field('Опис', config_name='extends')
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Зображення")
    slug = AutoSlugField(populate_from='name', unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Готове рішення'
        verbose_name_plural = 'Готові рішення'

           
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    description=CKEditor5Field('Описание', config_name='extends')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    slug = AutoSlugField(populate_from='name', unique=True, default='') 
    article = models.PositiveIntegerField(unique=True, verbose_name="Артикул")

    def __str__(self):
        return f"{self.name} - {self.article}"
        
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    description=CKEditor5Field('Описание', config_name='extends')
    slug = AutoSlugField(populate_from='name', unique=True, default='') 
    article = models.PositiveIntegerField(unique=True, verbose_name="Артикул")

    def __str__(self):
        return f"{self.name} - {self.article}"
        
    class Meta:
        verbose_name = 'Програмне забезпечення'
        verbose_name_plural = 'Програмне забезпечення'


class ProgramImage(models.Model):
    product = models.ForeignKey(Program, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Support(models.Model):
    name = models.CharField(max_length=150, unique=True)  
    description=CKEditor5Field('Опис', config_name='extends')
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Зображення")
    slug = AutoSlugField(populate_from='name', unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Технічна підтримка'
        verbose_name_plural = 'Технічна підтримка'


class Service(models.Model):
    name = models.CharField(max_length=150, unique=True)  
    description=CKEditor5Field('Опис', config_name='extends')
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Зображення")
    slug = AutoSlugField(populate_from='name', unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Сервісна підтримка'
        verbose_name_plural = 'Сервісна підтримка'


class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва проекту")  
    client = models.TextField(blank=True, verbose_name="Замовник")
    adress = models.TextField(blank=True, verbose_name="Адреса")
    realization_date = models.DateField(verbose_name="Дата реалізації")
    description=CKEditor5Field('Опис', config_name='extends')
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Зображення")
    slug = AutoSlugField(populate_from='name', unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Виконаний проект'
        verbose_name_plural = 'Виконані проекти'


class Offer(models.Model):
    OFFER_TYPES = (
        ('hardware', 'Железо'),
        ('software', 'Софт'),
        ('service', 'Сервіс'),
        ('support', 'Підтримка'),
    )

    name = models.CharField(max_length=150, verbose_name="Назва")
    description = CKEditor5Field('Опис', config_name='extends')
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Зображення")
    type = models.CharField(max_length=20, choices=OFFER_TYPES, verbose_name="Тип", default='hardware')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Пропозиція'
        verbose_name_plural = 'Пропозиції'


def generate_article():
    return random.randint(100000, 999999)

@receiver(pre_save, sender=Product)
def set_article(sender, instance, **kwargs):
    if instance._state.adding:  # Проверка, что это новый товар
        instance.article = generate_article()


