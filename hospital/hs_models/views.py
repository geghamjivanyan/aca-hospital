from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Patient, Doctor, Schedule

def patients(request):

    pl = Patient.objects.all()

    return render(request, 'patient.html', context={'patient_list': pl})

def doctors(request):

    dl = Doctor.objects.all()

    return render(request, 'doctor.html', context={'doctor_list': dl})

def schedules(request):

    sl = Schedule.objects.all()

    return render(request, 'schedule.html', context={'schedule_list': sl})

def add_new_patient(request):
    return render(request, 'new_patient.html')

