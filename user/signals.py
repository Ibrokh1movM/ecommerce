from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def after_user_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New user created: {instance}")
    else:
        print(f"User updated: {instance}")

@receiver(post_delete, sender=User)
def after_user_deleted(sender, instance, **kwargs):
    print(f"User deleted: {instance}")
