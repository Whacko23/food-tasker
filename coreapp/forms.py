from django import forms
from .models import Restaurant, User

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
            'email', 'website', 'cuisine_type', 'opening_hours', 'description'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email','username', 'password', 'first_name', 'last_name', 'phone_number'
        ]