from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="users/", blank=True, null=True)

    def __str__(self):
        return self.name