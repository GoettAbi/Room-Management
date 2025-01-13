# rooms/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),  # room_list.html anzeigen
    path('<int:id>/', views.room_detail, name='room_detail'),  # room_detail.html anzeigen
]
