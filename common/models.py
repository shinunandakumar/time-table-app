from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]

    TIME_SLOTS = [
        ('10-11', '10:00 AM - 11:00 AM'),
        ('11-12', '11:00 AM - 12:00 PM'),
        ('12-1', '12:00 PM - 1:00 PM'),
        ('1-2', '1:00 PM - 2:00 PM'),
        ('2-3', '2:00 PM - 3:00 PM'),
        ('3-4', '3:00 PM - 4:00 PM'),
        ('4-5', '4:00 PM - 5:00 PM'),
        ('5-6', '5:00 PM - 6:00 PM'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    time = models.CharField(max_length=5, choices=TIME_SLOTS)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.subject.name} on {self.day} at {self.time}"
