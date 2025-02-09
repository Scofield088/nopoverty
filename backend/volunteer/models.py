from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)  # Add this line
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
