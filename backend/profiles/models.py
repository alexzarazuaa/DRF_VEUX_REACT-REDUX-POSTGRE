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

<<<<<<< HEAD
    def book(self, bar):
        self.reference_booking.add(bar)
=======
    def book(self, bar, time):
        try:
            self.reference_booking.add(bar, through_defaults={'time':time})
        except Exception as e:
            print(e)
>>>>>>> 9f0eef014e084d42c87328ac3bb9d975da636c12
    
    def unbook(self, bar):
        self.reference_booking.remove(bar)
        
<<<<<<< HEAD
    def modbook(self, bar):
        self.reference_booking.remove(bar)

    def has_book(self, bar):
        return self.reference_booking.filter(pk=bar.pk).exists()
=======
    def modbook(self, bar, time):

        self.reference_booking.set([bar], through_defaults={'time':time})
>>>>>>> 9f0eef014e084d42c87328ac3bb9d975da636c12
        


class Booking(models.Model):
    class Meta:
<<<<<<< HEAD
         unique_together=(('person','bar'))
=======
            unique_together=(('person','bar','time'),)

>>>>>>> 9f0eef014e084d42c87328ac3bb9d975da636c12
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bar = models.ForeignKey('bars.Bar', on_delete=models.CASCADE)


