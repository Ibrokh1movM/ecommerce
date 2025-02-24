from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def after_product_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New product created: {instance}")
    else:
        print(f"Product updated: {instance}")

@receiver(post_delete, sender=Product)
def after_product_deleted(sender, instance, **kwargs):
    print(f"Product deleted: {instance}")
