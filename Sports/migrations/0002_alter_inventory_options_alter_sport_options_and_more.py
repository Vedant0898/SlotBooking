# Generated by Django 4.1 on 2022-08-26 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventory'},
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'verbose_name_plural': 'Sports'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'verbose_name_plural': 'Venues'},
        ),
    ]
