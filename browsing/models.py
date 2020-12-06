from django.db import models


class ItemOffer(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    owner = models.UUIDField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='ford.png')
