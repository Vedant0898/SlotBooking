# Generated by Django 4.1 on 2022-08-23 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('info', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Venue eg. Room No., Court No. etc', max_length=50)),
                ('no_of_courts', models.IntegerField(help_text='Number of courts available in this Venue')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sports.sport')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Equipment', max_length=100)),
                ('quantity', models.IntegerField()),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sports.sport')),
            ],
        ),
    ]