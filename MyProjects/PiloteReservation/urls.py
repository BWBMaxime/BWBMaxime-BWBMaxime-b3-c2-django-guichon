from django.urls import path
from PiloteReservation import views

urlpatterns = [
    path('', views.home, name='home'),
]