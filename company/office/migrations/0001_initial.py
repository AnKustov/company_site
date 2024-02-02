# Generated by Django 4.2.6 on 2023-11-11 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва компанії')),
                ('legal_name', models.CharField(max_length=200, verbose_name='Юридична назва')),
                ('edrpou', models.TextField(verbose_name='ЕДРПОУ')),
                ('physical_address', models.TextField(blank=True, verbose_name='Фізична адреса')),
                ('legal_address', models.TextField(verbose_name='Юридична адреса')),
                ('account', models.TextField(verbose_name='Розрахунковий рахунок')),
                ('tax_number', models.TextField(verbose_name='ІПН')),
                ('single_tax_payer_certificate', models.TextField(verbose_name='Свідоцтво платника єдиного податку, №')),
                ('phones', models.TextField(blank=True, help_text='Телефони', null=True, verbose_name='Телефон')),
                ('emails', models.TextField(blank=True, help_text='Электронні адреси', null=True, verbose_name='E-mail')),
                ('director', models.TextField(blank=True, verbose_name='Директор')),
                ('logo_image', models.ImageField(null=True, upload_to='images/', verbose_name='Логотип')),
                ('favicon', models.ImageField(null=True, upload_to='images/', verbose_name='favicon')),
            ],
            options={
                'verbose_name': 'Компанія',
                'verbose_name_plural': 'Компанії',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Департамент')),
                ('phones', models.TextField(blank=True, help_text='Телефони', null=True, verbose_name='Телефон')),
                ('emails', models.TextField(blank=True, help_text='Электронні адреси', null=True, verbose_name='E-mail')),
                ('manager', models.TextField(blank=True, null=True, verbose_name='Керівник')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменти',
            },
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Им'я користувача")),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефону')),
                ('email', models.EmailField(max_length=254, verbose_name='Електронна пошта')),
                ('message', models.TextField(verbose_name='Повідомлення')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('new', models.BooleanField(default=True, verbose_name='Нове')),
            ],
            options={
                'verbose_name': 'Повідомлення',
                'verbose_name_plural': 'Повідомлення',
            },
        ),
    ]
