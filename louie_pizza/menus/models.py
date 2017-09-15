from django.db import models

class MenuItemType(models.Model):
    item_type = models.CharField(max_length=255)

    def __str__(self):
        return self.item_type

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    item_type = models.ForeignKey(MenuItemType)

    def __str__(self):
        return self.name