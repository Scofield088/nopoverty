from django.urls import path
from .views import analyze_data

urlpatterns = [
    path('analysis/', analyze_data, name='analysis'),

]
