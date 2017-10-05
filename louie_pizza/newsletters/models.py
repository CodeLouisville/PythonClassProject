from django.db import models

class Subscriber(models.Model):
    date_subscribed = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.email