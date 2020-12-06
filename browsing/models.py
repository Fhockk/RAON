from django.db import models


class ItemOffer(models.Model):
    uuid = models.UUIDField()
    title = models.TextField()
    description = models.TextField()
    owner = models.UUIDField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    image = models.ImageField(default='ford.png')
