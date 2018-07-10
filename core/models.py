from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    key = models.CharField(max_length=18)
    secret = models.CharField(max_length=32)

    def get_token(self):
        pass
        # todo: get token from bitbucket

    def refresh_token(self):
        pass
        # todo: optional?

    def __str__(self):
        return str(self.user)
