from django.db import models

class Subscriber(models.Model):
    subscribed_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.TextField()

    def __str__(self):
        return self.name