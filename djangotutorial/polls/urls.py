from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "polls"  # Name der App für spätere Umkehr-URLs

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Startseite
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # Detailansicht einer Frage
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # Ergebnisse einer Frage
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Stimmabgabe
    path('calendar/', views.calendar_view, name='calendar'),  # Kalenderansicht
    path('overview/', views.overview, name='overview'),  # Verlinkung zur overview-View
    path('wishlist/', views.wishlist, name='wishlist'), # Verlinkung zur Wishlish
    path('cart/', views.cart, name='cart'),
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/', admin.site.urls),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








