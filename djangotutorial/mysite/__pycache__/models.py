from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('Konferenzraum', 'Konferenzraum'),
        ('Besprechungsraum', 'Besprechungsraum'),
        ('Arbeitsplatz', 'Arbeitsplatz'),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    amenities = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.CharField(max_length=100)  # For simplicity, storing the user's name
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return f"{self.room.name} booked by {self.user} on {self.date}"
