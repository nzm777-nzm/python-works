# Generated by Django 5.1.2 on 2024-11-04 14:20

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
                ('department', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('date_of_join', models.DateField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='employee_images')),
            ],
        ),
    ]
