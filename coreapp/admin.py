from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'cuisine_type')
    search_fields = ('name', 'city', 'cuisine_type')