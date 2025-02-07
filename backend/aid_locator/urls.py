from django.urls import path
from .views import aid_locator_view

urlpatterns = [
    path('', aid_locator_view, name='aidloc'),  # If template uses 'aidloc'
  # Make sure this matches the template
]


