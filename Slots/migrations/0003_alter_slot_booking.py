# Generated by Django 4.1 on 2022-08-27 05:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Slots', '0002_alter_schedule_day_alter_slot_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='booking',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]