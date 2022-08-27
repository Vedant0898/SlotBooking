# Generated by Django 4.1 on 2022-08-27 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Slots', '0004_alter_slot_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Slots.location'),
            preserve_default=False,
        ),
    ]