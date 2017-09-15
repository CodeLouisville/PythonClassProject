from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.item_type

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, related_name='items')

    def __str__(self):
        return self.name