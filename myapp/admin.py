from django.contrib import admin

# Register your models here.
from .models import hotel
# admin.site.register(hotel)

from .models import hotel, RoomBooking, FoodOrder

# Customize how RoomBookings are displayed
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'check_in', 'check_out', 'guests')
    list_filter = ('room_type', 'check_in')
    search_fields = ('name', 'email', 'phone')

# Customize how FoodOrders are displayed
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'order_date', 'order_time', 'total_cost')
    list_filter = ('order_date',)
    search_fields = ('customer_name', 'phone_number')

# Register your models with the admin site
admin.site.register(hotel)
admin.site.register(RoomBooking, RoomBookingAdmin)
admin.site.register(FoodOrder, FoodOrderAdmin)