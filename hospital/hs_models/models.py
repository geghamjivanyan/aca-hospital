from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=6)
    age = models.IntegerField(default=18)

    def __str__(self):
        return "{} {} - {} {}".format(self.user.first_name, self.user.last_name, self.gender, self.age)

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discipline = models.CharField(max_length=30)

    def __str__(self):
        return "{} {} - {}".format(self.user.first_name, self.user.last_name, self.discipline)

class Schedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    meet_time = models.DateTimeField()

    def __str__(self):
        return "{} {} {}".format(self.patient, self.doctor, self.meet_time)



