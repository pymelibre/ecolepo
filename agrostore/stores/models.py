from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=255)
    legal_id = models.CharField(max_length=10)

    def __str__(self):
        return self.name
