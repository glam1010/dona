from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt


def mpesa_payment(request):
    # MPesa payment processing code
    return JsonResponse({"message": "Payment processed"})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Replace with your homepage URL name
        else:
            messages.error(request, "Invalid username or password")
            pass
    return render(request, "login_register.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = UserCreationForm()
        pass
    return render(request, "register.html", {"form": form})
def donate_view(request):
    if request.method == 'POST':
        donation_amount = request.POST.get('donation_amount')
        # Handle donation logic here (save to database, process payment, etc.)
        return HttpResponse(f"Thank you for donating ${donation_amount}")
    return render(request, 'donate.html')

