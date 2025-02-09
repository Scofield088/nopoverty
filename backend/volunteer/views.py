from django.shortcuts import render
from django.http import JsonResponse
from .models import Volunteer

def volunteer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if not name or not email or not phone:
            return JsonResponse({"error": "All fields are required!"}, status=400)

        try:
            Volunteer.objects.create(name=name, email=email, phone=phone, message=message)
            return JsonResponse({"message": "Volunteer data saved successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "volunteer.html")
