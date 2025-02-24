from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(
        "Email Address",
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"Profile of {self.user.email}"


