from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
            'email', 'website', 'cuisine_type', 'opening_hours', 'description'
        ]
