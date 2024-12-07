from django.shortcuts import render
import requests
from django.http import JsonResponse

from django.conf import settings
from paypalrestsdk import Payment
from django.http import JsonResponse
from django.conf import settings

import paypalrestsdk
paypalrestsdk.configure({
    "mode": "sandbox",  # Use "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})

def paypal_payment(request):
    """
    Handle PayPal payment request
    """
    if request.method == 'POST':
        # Create a payment object
        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": "10.00",
                    "currency": "USD"
                },
                "description": "Donation"
            }],
            "redirect_urls": {
                "return_url": "https://yourdomain.com/payment-success",
                "cancel_url": "https://yourdomain.com/payment-cancel",
            }
        })

        if payment.create():
            for link in payment['links']:
                if link['rel'] == 'approval_url':
                    return JsonResponse({"approval_url": link['href']})
        else:
            return JsonResponse({"error": payment.error}, status=400)

    return JsonResponse({"message": "Invalid request method"}, status=400)


@csrf_exempt
def mpesa_payment(request):
    """
    Handle MPesa payment request
    """
    if request.method == 'POST':
        # Get access token
        url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        response = requests.get(url, auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
        access_token = response.json()['access_token']

        # Process the payment
        payment_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        payload = {
            "BusinessShortCode": "174379",  # Test shortcode
            "Password": "base64_encoded_password",  # Generated using shortcode, passkey, and timestamp
            "Timestamp": "timestamp",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 100,  # Amount to charge
            "PartyA": "254712345678",  # User phone number
            "PartyB": "174379",  # Test shortcode
            "PhoneNumber": "254712345678",
            "CallBackURL": "https://yourdomain.com/callback",
            "AccountReference": "Donation",
            "TransactionDesc": "Payment for donation",
        }
        payment_response = requests.post(payment_url, json=payload, headers=headers)

        return JsonResponse({"message":"Payment processed"})

    return JsonResponse({"message": "Invalid request method"}, status=400)


# Create your views here.
