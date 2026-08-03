from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm


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