#from django.shortcuts import render, get_object_or_404
#from .models import Room
#from django.db import models

#def room_list(request):
    #rooms = [
    #    {'id': 1, 'name': 'Test Room', 'capacity': 10, 'amenities': 'Whiteboard, Projector'},
    #    {'id': 2, 'name': 'Another Room', 'capacity': 20, 'amenities': 'TV, Coffee Machine'}
    #]
    #return render(request, 'room/room_list.html', {'rooms': rooms})

#def room_detail(request, id):
    #room = {'id': id, 'name': 'Test Room', 'capacity': 10, 'amenities': 'Whiteboard, Projector'}
    #return render(request, 'room/room_detail.html', {'room': room})

#class Room(models.Model):
#    name = models.CharField(max_length=100)
#    capacity = models.IntegerField()
#    amenities = models.TextField()
#    image_url = models.URLField(blank=True, null=True)
#
#    def __str__(self):
#        return self.name
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hallo, dies ist meine Website!")




