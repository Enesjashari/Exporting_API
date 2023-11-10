# Generated by Django 4.2.7 on 2023-11-02 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_quote_actor_name_alter_quote_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='actor_name',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='author_bio',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='category',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='context',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='language',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='movie_title',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='publish_date',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='rating',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]