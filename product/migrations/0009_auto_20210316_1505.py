# Generated by Django 2.2 on 2021-03-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]