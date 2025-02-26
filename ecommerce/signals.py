from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Product
import json
import os


@receiver(post_save, sender=Product)
def after_product_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New product created: {instance}")
    else:
        print(f"Product updated: {instance}")

# @receiver(post_delete, sender=Product)
# def after_product_deleted(sender, instance, **kwargs):
#     print(f"Product deleted: {instance}")


DATA_FILE = "deleted_products.json"


def save_deleted_product(data):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                products = json.load(file)
            except json.JSONDecodeError:
                products = {}
    else:
        products = {}

    products[data["name"]] = data

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


@receiver(pre_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    product_data = {
        "name": instance.name,
        "price": float(instance.price),
        "description": instance.description,
        "deleted_at": instance.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    }
    save_deleted_product(product_data)
    print(f'Product "{instance.name}" deleted and saved to JSON')
