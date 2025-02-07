from django.shortcuts import render

def volunteer(request):
    return render(request, 'volunteer.html')  # ✅ Ensure it's correct
