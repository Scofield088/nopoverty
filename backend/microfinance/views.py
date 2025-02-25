from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import LoanApplication  # Import LoanApplication model (you need to create this in models.py)
from .forms import LoanApplicationForm  # Import the form (define in forms.py)

def microfinance_home(request):
    return render(request, 'microfinance.html')

def check_eligibility(request):
    if request.method == "POST":
        age = int(request.POST.get("age", 0))
        income = float(request.POST.get("income", 0))
        
        # Simple eligibility criteria
        eligible = age >= 18 and income <= 5000
        return JsonResponse({"eligible": eligible})
    
    return JsonResponse({"error": "Invalid request"}, status=400)

def apply_for_loan(request):
    if request.method == "POST":
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Application submitted successfully!"})
        return JsonResponse({"error": "Invalid data provided."})
    
    return JsonResponse({"error": "Invalid request"}, status=400)
