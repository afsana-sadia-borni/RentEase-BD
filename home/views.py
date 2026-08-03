from django.shortcuts import render, redirect
 proma-working-code
from .models import Property
from .forms import PropertyForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
 main

# ১. ইউজার রেজিস্ট্রেশন ভিউ
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # অ্যাকাউন্ট তৈরির পর অটোমেটিক লগইন হয়ে যাবে
            messages.success(request, "Registration successful!")
            return redirect('property_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

 proma-working-code
def home(request):
    properties = Property.objects.all()

    return render(request, 'home/index.html', {
        'properties': properties
    })


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PropertyForm()

    return render(request, 'home/add_property.html', {
        'form': form
    })

# ২. ইউজার লগইন ভিউ
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('property_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ৩. ইউজার লগআউট ভিউ
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

# ৪. সাময়িক হোমপেজ ভিউ (টেস্টিংয়ের জন্য)
def property_list_view(request):
    return render(request, 'property_list.html')
 main
