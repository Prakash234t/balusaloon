from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} ({self.phone})"
