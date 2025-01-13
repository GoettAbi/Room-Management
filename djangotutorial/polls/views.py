from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from .models import Room, Reservation, Question

# Startseite (Home-Seite)
def home(request):
    rooms = Room.objects.all()
    return render(request, 'polls/HOME.html', {'rooms': rooms})

# Übersicht der Räume
def room_overview(request):
    rooms = Room.objects.all()
    return render(request, 'polls/overview.html', {'rooms': rooms})

# Kalenderansicht
def calendar_view(request):
    return render(request, 'polls/calendar.html')

# Wunschliste (Beispielansicht)
def wishlist(request):
    return render(request, 'polls/wishlist.html')

# Index-Seite für die Umfragen
class IndexView(TemplateView):
    template_name = "polls/index.html"

# Detailansicht einer Frage
class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"

# Ergebnisse einer Frage anzeigen
class ResultsView(DetailView):
    model = Question
    template_name = "polls/results.html"

# Admin-Dashboard, nur zugänglich für Benutzer mit Staff-Status
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')  # Benutzer ohne Staff-Status zur Startseite weiterleiten

    return render(request, 'polls/admin_dashboard.html')

# Admin-Überblick der Reservierungen
def admin_overview(request):
    reservations = Reservation.objects.all().order_by('date')
    return render(request, 'polls/admin_overview.html', {'reservations': reservations})

# Login-View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Ungültige Anmeldedaten'})
    return render(request, 'login.html')

# Weitere Views
def vote(request, question_id):
    return render(request, 'polls/vote.html')

def overview(request):
    return render(request, 'polls/overview.html')

def cart(request):
    return render(request, 'polls/cart.html')

def index(request):
    return render(request, 'polls/index.html')

from django.http import HttpResponse
from django.conf import settings
import os

def test_media(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "computerraum.jpg")
    file_path = os.path.join(settings.MEDIA_ROOT, "computerraum2.jpg")
    file_path = os.path.join(settings.MEDIA_ROOT, "Grundriss Computerraum.jpg")
    if os.path.exists(file_path):
        return HttpResponse(f"File exists at: {file_path}")
    else:
        return HttpResponse("File not found.")

