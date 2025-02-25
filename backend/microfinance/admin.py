from django.contrib import admin
from .models import LoanApplication

class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'loan_amount', 'applied_on')
    search_fields = ('name', 'business_idea')
    list_filter = ('applied_on',)

admin.site.register(LoanApplication, LoanApplicationAdmin)
