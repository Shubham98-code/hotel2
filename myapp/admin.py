from django.contrib import admin
from .models import RoomBooking, FoodOrder, ContactMessage # Removed hotel

# Customize how RoomBookings are displayed
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'check_in', 'check_out', 'guests', 'status')
    list_filter = ('room_type', 'check_in', 'status')
    search_fields = ('name', 'email', 'phone')

# Customize how FoodOrders are displayed
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'order_date', 'order_time', 'total_cost', 'status')
    list_filter = ('order_date', 'status')
    search_fields = ('customer_name', 'phone_number')

# Customize Contact Messages
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')

# Register your models
admin.site.register(RoomBooking, RoomBookingAdmin)
admin.site.register(FoodOrder, FoodOrderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin) # Added this