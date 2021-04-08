from django.db import models

from core.models import TimestampedModel


class Bar(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    name = models.CharField(db_index=True, max_length=255)

    description = models.TextField()

    owner = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='bars'
    )
    
    reference_booking = models.ManyToManyField('profiles.Profile', through='profiles.Booking')

    def __str__(self):
        return self.name
