from django.db import models

class CustomerFeedback(models.Model):
    date_submitted = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    date_of_visit = models.DateField()
    email = models.EmailField()
    title = models.CharField(max_length=25)
    message = models.CharField(max_length=750)

    def __str__(self):
        return "Message from {0}: {1}".format(self.name, self.title)