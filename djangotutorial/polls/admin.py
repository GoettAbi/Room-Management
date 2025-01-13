from django.contrib import admin
from .models import Room, Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'booked_by', 'date')  # 'booked_by' korrekt definiert
    list_filter = ('room', 'date')
    search_fields = ('booked_by',)

    def booked_by(self, obj):
        """
        Gibt den Benutzer oder eine andere Information zurück,
        die beschreibt, wer die Reservierung vorgenommen hat.
        """
        return obj.user.username if hasattr(obj, 'user') and obj.user else "Unbekannt"
    booked_by.short_description = 'Booked By'  # Optional: Benutzerfreundlicher Name für die Admin-Oberfläche
