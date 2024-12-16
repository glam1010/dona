from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# User Profile
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
def donate_view(request):
    if request.method == 'POST':
        # Get the JSON data from the request
        data = json.loads(request.body)  # Load the incoming JSON data
        amount = data.get('amount')  # Retrieve the 'amount' from the POST data

        # Process the donation or any other logic here
        # Example: Save the donation to the database
        # Donation.objects.create(amount=amount)

        # Send a JSON response with a success message
        return JsonResponse({'message': 'Donation successful!', 'amount': amount})

    # Return an error message if the method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=400)