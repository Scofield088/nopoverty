from django.urls import path
from .views import microfinance_home, check_eligibility, apply_for_loan

urlpatterns = [
    path('', microfinance_home, name='microfinance_home'),
    path('check-eligibility/', check_eligibility, name='check_eligibility'),
    path('apply/', apply_for_loan, name='apply_for_loan'),
]
