from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

class Driver(models.Model):
    """A driver for our cabbie app.
    """

    ACTIVE = 'A'
    INACTIVE = 'I'
    DRIVER_STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive')
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    status = models.CharField(
        max_length=1, 
        choices=DRIVER_STATUS_CHOICES,
    )
    mentor = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name='mentees',
        limit_choices_to={'status': ACTIVE},
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def clean(self):
        if self.mentor and self.id == self.mentor.id:
            raise ValidationError(
                {'mentor': "Sorry, you can't be your own mentor."}
            )

    def clean_fields(self, exclude=None):
        if self.mentor and self.mentor.status != self.ACTIVE:
            raise ValidationError(
                {'mentor': "Sorry, you can't choose that mentor."}
            )            

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.status == self.INACTIVE:
            for mentee in self.mentees.all():
                mentee.mentor = None
                mentee.save()
        super(Driver, self).save(*args, **kwargs)

class Description(models.Model):
    """A description that can be applied to a driver.

    Examples: friendly, funny, quiet, talkative, dangerous
    """
    title = models.SlugField(max_length=50, unique=True,)
    drivers = models.ManyToManyField(
        Driver, 
        related_name='descriptions',
        limit_choices_to={'status': Driver.ACTIVE},)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        self.title = self.title.lower()
        super(Description, self).save(*args, **kwargs)

class Counter(models.Model):
    """A description that can be applied to a driver.

    Examples: friendly, funny, quiet, talkative, dangerous
    """
    name = models.CharField(max_length=255, default='')
    count = models.IntegerField()

    def __str__(self):
        return str(self.count)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Counter, self).save(*args, **kwargs)