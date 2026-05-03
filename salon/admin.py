from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('service', 'created_at')
