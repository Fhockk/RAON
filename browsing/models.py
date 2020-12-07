from django.db import models
from django.contrib.auth.models import User


class ItemOffer(models.Model):
    uuid = models.UUIDField()
    title = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    image = models.ImageField(default='ford.png')
