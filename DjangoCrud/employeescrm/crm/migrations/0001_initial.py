# Generated by Django 5.1.2 on 2024-10-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
