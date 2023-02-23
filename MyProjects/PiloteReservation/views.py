from django.shortcuts import render
from PiloteReservation.models import Reservation
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages

def home(request):
    heures = ['9h','10h','11h','12h','13h','14h','15h','16h','17h','18h']
      #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(15)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)
    

    if request.method == 'POST':
        service = request.POST.get('service')
        jour = request.POST.get('jour')

        request.session['jour'] = jour
        request.session['service'] = service



    return render(request, 'home.html', {
            'weekdays':weekdays,
            'validateWeekdays':validateWeekdays,
            'heures':heures
        })
    
def validWeekday(jours):
    ajourdhui = datetime.now()
    weekdays = []
    for i in range (0, jours):
        x = ajourdhui + timedelta(days=i)
        y = x.strftime('%A')
        weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Reservation.objects.filter(jour=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

