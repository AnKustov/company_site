# Generated by Django 4.2.6 on 2023-11-12 20:48

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_delete_feedbackmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Історія компанії')),
            ],
            options={
                'verbose_name': 'Історія компанії',
                'verbose_name_plural': 'Історія компанії',
            },
        ),
    ]
