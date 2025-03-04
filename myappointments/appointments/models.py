# appointments/models.py
from django.db import models
from django.conf import settings

class Appointment(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"
