# Generated by Django 4.2.7 on 2023-11-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=10000)),
                ('name', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
    ]