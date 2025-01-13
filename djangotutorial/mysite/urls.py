##from django.contrib import admin
#from django.urls import path, include
#from django.http import HttpResponse

#def home(request):
#    return HttpResponse("Room Management System!")  

#from django.contrib import admin
#from django.urls import path, include
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('polls.urls')),  # Main URLs der App polls
#    path('rooms/', include('rooms.urls')),  # Richtet rooms auf rooms/urls.py
#]
#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.room_list, name='room_list'),  # Zeigt die room_list.html
#    path('<int:id>/', views.room_detail, name='room_detail'),  # Zeigt room_detail.html
#]
from django.contrib import admin
from django.urls import path, include
from polls import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Leitet direkt auf die Index-View weiter
    path('polls/', include('polls.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






