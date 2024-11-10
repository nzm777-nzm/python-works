# Generated by Django 5.1.2 on 2024-10-22 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('varient', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('fuel_type', models.CharField(choices=[('petrol', 'petrol'), ('CNG', 'CNG'), ('EV', 'EV'), ('diesel', 'diesel')], default='petrol', max_length=200)),
                ('running_km', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('owner_type', models.CharField(choices=[('single', 'single'), ('second', 'second'), ('other', 'other')], default='single', max_length=200)),
            ],
        ),
    ]
