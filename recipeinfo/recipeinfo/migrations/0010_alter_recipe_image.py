# Generated by Django 5.0.3 on 2024-03-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeinfo', '0009_recipe_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipeinfo/static/'),
        ),
    ]