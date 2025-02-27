# Generated by Django 5.1.5 on 2025-02-27 07:02

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='UZ'),
        ),
    ]
