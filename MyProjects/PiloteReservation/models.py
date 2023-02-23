from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

ECOLE = (
    ("Ecole de la comédie", "Ecole de la comédie"),
    ("Ecole de Saint-Eloi", "Ecole de Saint-Eloi"),
    ("Ecole de Port Marianne", "Ecole de Port Marianne"),
    ("Ecole de Saint-Jean-De-Védas", "Ecole de Saint-Jean-De-Védas"),
    )

SERVICE = (
    ("Voiture", "Voiture"),
    ("Moto", "Moto"),
    ("Avion", "Avion"),
    ("Bateau", "Bateau"),
    )

HEURES = (
    ("9h", "9h"),
    ("10h", "10h"),
    ("11h", "11h"),
    ("12h", "12h"),
    ("13h", "13h"),
    ("14h", "14h"),
    ("15h", "15h"),
    ("16h", "16h"),
    ("17h", "17h"),
    ("18h", "18h"),
)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ecole = models.CharField(max_length=50, choices=ECOLE, default="Ecole de la comédie")
    service = models.CharField(max_length=50, choices=SERVICE, default="Voiture")
    jour = models.DateField(default=datetime.now)
    heure = models.CharField(max_length=10, choices=HEURES, default="9h")
    temps_command = models.DateTimeField(default=datetime.now, blank=True)
   