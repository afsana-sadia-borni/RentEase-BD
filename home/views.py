from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Property
from .forms import PropertyForm



def home(request):

    properties = Property.objects.all()

    return render(request, 'home/index.html', {
        'properties': properties
    })



def properties(request):

    properties = Property.objects.all()

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





def user_logout(request):

    logout(request)

    return redirect('/')