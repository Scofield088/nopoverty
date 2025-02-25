from django.db import models

class LoanApplication(models.Model):
    name = models.CharField(max_length=100)
    business_idea = models.TextField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contact_details = models.CharField(max_length=100)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
