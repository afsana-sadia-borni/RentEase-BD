from django import forms
from .models import Property, Booking


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title',
            'location',
            'rent',
            'property_type',
            'is_available',
            'description',
            'image',
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'booking_date',
        ]

        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            )
        }