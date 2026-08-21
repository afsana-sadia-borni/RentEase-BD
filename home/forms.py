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
            'payment_method','phone_number', 'transaction_id'
        ]

        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 01700000000'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. TRX12345678'}),
            
            
        }