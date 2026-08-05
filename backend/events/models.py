from django.db import models
from django.utils.text import slugify


class Event(models.Model):
    TYPE_MEETUP = 'meetup'
    TYPE_WORKSHOP = 'workshop'
    TYPE_WEBINAR = 'webinar'
    TYPE_CONFERENCE = 'conference'
    TYPE_OTHER = 'other'
    TYPE_CHOICES = [
        (TYPE_MEETUP, 'Meetup'),
        (TYPE_WORKSHOP, 'Workshop'),
        (TYPE_WEBINAR, 'Webinar'),
        (TYPE_CONFERENCE, 'Conference'),
        (TYPE_OTHER, 'Other'),
    ]

    STATUS_UPCOMING = 'upcoming'
    STATUS_ONGOING = 'ongoing'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = [
        (STATUS_UPCOMING, 'Upcoming'),
        (STATUS_ONGOING, 'Ongoing'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_UPCOMING)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
