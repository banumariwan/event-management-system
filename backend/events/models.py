from django.db import models
from accounts.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tasks")
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)



class Attendance(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff.username} - {self.event.name}"