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

    reference_booking = models.ManyToManyField(
        'bars.Bar', 
        through='Booking',
        related_name='booking_by')


    def favorite(self, bar):
        self.favorites.add(bar)

    def unfavorite(self, bar):
        self.favorites.remove(bar)

    def has_favorited(self, bar):
        return self.favorites.filter(pk=bar.pk).exists()


    def book(self, bar):
        self.reference_booking.add(bar)

    def book(self, bar):
        try:
            self.reference_booking.add(bar)
        except Exception as e:
            print(e)

    
    def unbook(self, bar):
        self.reference_booking.remove(bar)
        

    def modbook(self, bar):
        self.reference_booking.remove(bar)

    def has_book(self, bar):
        return self.reference_booking.filter(pk=bar.pk).exists()

    def modbook(self, bar):

        self.reference_booking.set([bar])

        


class Booking(models.Model):
    class Meta:
         unique_together=(('person','bar'))

    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bar = models.ForeignKey('bars.Bar', on_delete=models.CASCADE)


