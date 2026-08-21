from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Property, Booking, Payment, Profile
from .forms import PropertyForm, BookingForm, PaymentForm
from .models import Property, Review


def home(request):
    properties = Property.objects.all()[:6]
    return render(request, 'home/index.html', {
        'properties': properties
    })


def properties(request):
    properties = Property.objects.all()
    search = request.GET.get('search')
    max_rent = request.GET.get('max_rent')

    if search:
        properties = properties.filter(location__icontains=search)

    if max_rent:
        properties = properties.filter(rent__lte=max_rent)

    return render(request, 'home/properties.html', {
        'properties': properties
    })


@login_required
def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            
            # ম্যাপের Lat/Lng সেভ করা
            property_obj.latitude = request.POST.get('latitude')
            property_obj.longitude = request.POST.get('longitude')
            
            property_obj.save()
            messages.success(request, "প্রপার্টিটি সফলভাবে যুক্ত করা হয়েছে!")
            return redirect('my_properties')
    else:
        form = PropertyForm()

    return render(request, 'home/add_property.html', {
        'form': form
    })


def property_detail(request, id):
    property_obj = get_object_or_404(Property, id=id)
    user_booking = None
    is_owner = False

    if request.user.is_authenticated:
        
        if property_obj.owner == request.user:
            is_owner = True
        
        
        user_booking = Booking.objects.filter(property=property_obj, user=request.user).first()

    context = {
        'property': property_obj,
        'user_booking': user_booking,
        'is_owner': is_owner,
    }
    return render(request, 'home/property_detail.html', context)


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'tenant')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'home/register.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        Profile.objects.create(user=user, role=role)
        messages.success(request, "অ্যাকোউন্ট সফলভাবে তৈরি হয়েছে! অনুগ্রহ করে লগইন করুন।")
        return redirect('login')

    return render(request, 'home/register.html')


@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"স্বাগতম {user.username}! সফলভাবে লগইন করা হয়েছে।")
            return redirect('home')
        else:
            messages.error(request, 'ইউজারনেম বা পাসওয়ার্ড ভুল হয়েছে!')
            return render(request, 'home/login.html', {'error': 'Invalid username or password'})

    return render(request, 'home/login.html')


@login_required
def profile(request):
    return render(request, 'home/profile.html')


@login_required
def my_properties(request):
    properties = Property.objects.filter(owner=request.user)
    return render(request, 'home/my_properties.html', {
        'properties': properties
    })


@login_required
def edit_property(request, id):
    property_obj = get_object_or_404(Property, id=id, owner=request.user)

    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "প্রপার্টির তথ্য সফলভাবে আপডেট করা হয়েছে!")
            return redirect('my_properties')
    else:
        form = PropertyForm(instance=property_obj)

    return render(request, 'home/edit_property.html', {
        'form': form,
        'property': property_obj
    })


@login_required
def delete_property(request, id):
    property_obj = get_object_or_404(Property, id=id, owner=request.user)

    if request.method == "POST":
        property_obj.delete()
        messages.success(request, "প্রপার্টিটি সফলভাবে ডিলিট করা হয়েছে!")
        return redirect('my_properties')

    return render(request, 'home/delete_property.html', {
        'property': property_obj
    })


def contact_owner(request, id):
    property_obj = get_object_or_404(Property, id=id)

    if not property_obj.owner:
        return redirect('property_detail', id=id)

    return render(request, 'home/contact_owner.html', {
        'property': property_obj
    })


@login_required
def book_property(request, id):
    property_obj = get_object_or_404(Property, id=id)

    if not property_obj.is_available:
        messages.warning(request, 'This property is not available.')
        return render(request, 'home/booking.html', {
            'property': property_obj
        })

    existing_booking = Booking.objects.filter(
        property=property_obj,
        user=request.user,
        status__in=['Pending', 'Confirmed']
    ).exists()

    if existing_booking:
        messages.warning(request, 'You already have an active booking for this property.')
        return render(request, 'home/booking.html', {
            'property': property_obj
        })

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property_obj
            booking.user = request.user
            booking.save()
            messages.success(request, "বুকিং রিকোয়েস্ট সফলভাবে পাঠানো হয়েছে!")
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'home/booking.html', {
        'form': form,
        'property': property_obj
    })


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'home/my_booking.html', {
        'bookings': bookings
    })


@login_required
def make_payment(request, id):
    booking = get_object_or_404(Booking, id=id, user=request.user)

    if booking.status != 'Confirmed':
        messages.error(request, 'Payment is only available for confirmed bookings.')
        return redirect('my_bookings')

    if Payment.objects.filter(booking=booking).exists():
        messages.warning(request, 'Payment has already been made for this booking.')
        return redirect('my_bookings')

    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.amount = booking.property.rent
            payment.status = 'Paid'
            payment.save()
            messages.success(request, "🎉 পেমেন্ট সফলভাবে সম্পন্ন হয়েছে (Dummy Payment)!")
            return redirect('my_bookings')
    else:
        form = PaymentForm()

    return render(request, 'home/payment.html', {
        'form': form,
        'booking': booking
    })


@login_required
def owner_bookings(request):
    bookings = Booking.objects.filter(property__owner=request.user).order_by('-created_at')
    return render(request, 'home/owner_bookings.html', {
        'bookings': bookings
    })


@login_required
def confirm_booking(request, id):
    booking = get_object_or_404(Booking, id=id, property__owner=request.user)
    booking.status = 'Confirmed'
    booking.save()
    property_obj = booking.property
    property_obj.is_available = False
    property_obj.save()
    messages.success(request, f"{booking.user.username}-এর বুকিং রিকোয়েস্ট কনফার্ম করা হয়েছে!")
    return redirect('owner_bookings')


@login_required
def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id, property__owner=request.user)
    booking.status = 'Cancelled'
    booking.save()
    property_obj = booking.property
    property_obj.is_available = True
    property_obj.save()
    messages.error(request, f"{booking.user.username}-এর বুকিং রিকোয়েস্ট বাতিল করা হয়েছে।")
    return redirect('owner_bookings')


def user_logout(request):
    logout(request)
    messages.info(request, "সফলভাবে লগআউট করা হয়েছে।")
    return redirect('home')
@login_required
def add_review(request, property_id):
    if request.method == 'POST':
        property_obj = get_object_or_404(Property, id=property_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if rating and comment:
            Review.objects.create(
                property=property_obj,
                user=request.user,
                rating=rating,
                comment=comment
            )
            messages.success(request, "আপনার রিভিউ সফলভাবে যুক্ত হয়েছে!")
        else:
            messages.error(request, "সবগুলো ফিল্ড সঠিকভাবে পূরণ করুন।")

    return redirect('property_detail', id=property_id) # আপনার Property Detail URL এর নাম দিন
