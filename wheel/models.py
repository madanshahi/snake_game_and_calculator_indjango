# wheel/models.py
from django.db import models

class SpinResult(models.Model):
    user = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)
    spin_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} won {self.prize}"
