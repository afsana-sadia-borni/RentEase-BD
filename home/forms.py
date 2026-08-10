from django import forms
from .models import Property


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