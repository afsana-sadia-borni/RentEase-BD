from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Property, Booking
from .forms import PropertyForm, BookingForm


def home(request):

    properties = Property.objects.all()

    return render(request, 'home/index.html', {
        'properties': properties
    })


def properties(request):

    properties = Property.objects.all()

    search = request.GET.get('search')
    max_rent = request.GET.get('max_rent')

    if search:
        properties = properties.filter(
            location__icontains=search
        )

    if max_rent:
        properties = properties.filter(
            rent__lte=max_rent
        )

    return render(request, 'home/properties.html', {
        'properties': properties
    })


def add_property(request):

    if request.method == "POST":

        form = PropertyForm(request.POST, request.FILES)

        if form.is_valid():

            property = form.save(commit=False)

            if request.user.is_authenticated:
                property.owner = request.user

            property.save()

            return redirect('/')

    else:

        form = PropertyForm()

    return render(request, 'home/add_property.html', {
        'form': form
    })


def property_detail(request, id):

    property = Property.objects.get(id=id)

    return render(request, 'home/property_detail.html', {
        'property': property
    })


def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            return render(request, 'home/register.html', {
                'error': 'Username already exists!'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('/login/')

    return render(request, 'home/register.html')


def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('/')

        else:

            return render(request, 'home/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'home/login.html')


def profile(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    return render(request, 'home/profile.html')


def my_properties(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    properties = Property.objects.filter(
        owner=request.user
    )

    return render(request, 'home/my_properties.html', {
        'properties': properties
    })


def edit_property(request, id):

    property = Property.objects.get(
        id=id,
        owner=request.user
    )

    if request.method == "POST":

        form = PropertyForm(
            request.POST,
            request.FILES,
            instance=property
        )

        if form.is_valid():

            form.save()

            return redirect('/my-properties/')

    else:

        form = PropertyForm(instance=property)

    return render(request, 'home/edit_property.html', {
        'form': form,
        'property': property
    })


def delete_property(request, id):

    property = Property.objects.get(
        id=id,
        owner=request.user
    )

    if request.method == "POST":

        property.delete()

        return redirect('/my-properties/')

    return render(request, 'home/delete_property.html', {
        'property': property
    })


def contact_owner(request, id):

    property = Property.objects.get(id=id)

    if not property.owner:
        return redirect('/property/{}/'.format(id))

    return render(request, 'home/contact_owner.html', {
        'property': property
    })


def book_property(request, id):

    property = Property.objects.get(id=id)

    if not request.user.is_authenticated:
        return redirect('/login/')

    if not property.is_available:

        return render(request, 'home/booking.html', {
            'property': property,
            'error': 'This property is not available.'
        })

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.property = property
            booking.user = request.user

            booking.save()

            return redirect('/my-bookings/')

    else:

        form = BookingForm()

    return render(request, 'home/booking.html', {
        'form': form,
        'property': property
    })


def my_bookings(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'home/my_bookings.html', {
        'bookings': bookings
    })


def user_logout(request):

    logout(request)

    return redirect('/')