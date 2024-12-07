from django.urls import path
from .views import mpesa_payment, paypal_payment

urlpatterns = [
    path('mpesa/', mpesa_payment, name='mpesa_payment'),
    path('paypal/', paypal_payment, name='paypal_payment'),
]
