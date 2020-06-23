from django.db import models

class User(models.Model):
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.token
