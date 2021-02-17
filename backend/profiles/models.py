from django.db import models
from core.models import TimestampedModel

class Profile(TimestampedModel):
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username

    favorites = models.ManyToManyField(
        'bars.Bar',
        related_name='favorited_by'
    )

    reference_booking = models.ManyToManyField('bars.Bar', through='Booking')


    def favorite(self, bar):
        """Favorite `bar` if we haven't already favorited it."""
        self.favorites.add(bar)

    def unfavorite(self, bar):
        """Unfavorite `bar` if we've already favorited it."""
        self.favorites.remove(bar)

    def has_favorited(self, bar):
        """Returns True if we have favorited `bar`; else False."""
        return self.favorites.filter(pk=bar.pk).exists()

class Booking(models.Model):
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bar = models.ForeignKey('bars.Bar', on_delete=models.CASCADE)
    date_joined = models.DateField()
