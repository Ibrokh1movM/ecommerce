# Generated by Django 5.1.5 on 2025-02-13 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_customer_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_image',
            field=models.ImageField(default='media/team/avatar.png', upload_to='media/customers/img'),
        ),
    ]
