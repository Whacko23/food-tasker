from django.contrib import admin
from .models import Restaurant, UserProfile, Customer, Driver   

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'user__email', 'phone_number')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'cuisine_type')
    search_fields = ('name', 'city', 'cuisine_type')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    search_fields = ('user__username', 'user__email', 'avatar')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    search_fields = ('user__username', 'user__email', 'avatar')


