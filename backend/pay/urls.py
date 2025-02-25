# from django.urls import path
# from .views import donate, payment_success

# urlpatterns = [
#     path("pay/", donate, name="pay"),
#     path("payment-success/", payment_success, name="payment_success"),
# ]
from django.urls import path
from .views import donate, donate_general, payment_success

urlpatterns = [
    path("", donate, name="pay"),                    # Specific Disaster Relief Donation
    path("general/", donate_general, name="donate"), # General Donation Page
    path("success/", payment_success, name="payment_success"),  # Payment success callback
]