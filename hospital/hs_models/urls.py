from django.urls import path

from . import views

urlpatterns = [
    path('patients/', views.patients),
    path('doctors/', views.doctors),
    path('schedule/', views.schedules),
    path('patient/', views.add_new_patient)
]

