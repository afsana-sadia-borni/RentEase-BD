from django import forms
from .models import Property, Booking, Payment


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


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = [
            'payment_method',
        ]

        widgets = {
            'payment_method': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }