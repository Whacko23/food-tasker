from django import forms
from .models import Restaurant, UserProfile
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name', 'address', 'city', 'state', 'zip_code', 'phone_number',
            'email', 'website', 'cuisine_type', 'opening_hours', 'description','logo'
        ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = [
            'email', 'username', 'password', 'first_name', 'last_name'
        ]
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user