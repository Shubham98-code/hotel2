from django.db import models

# --- DELETED: class hotel(models.Model) ---

# --- NEW: Model to save Contact Form messages ---
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class RoomBooking(models.Model):
    # --- Status Fields ---
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    guests = models.IntegerField()
    room_type = models.CharField(max_length=50)
    check_in = models.DateField()
    check_out = models.DateField()
    requests = models.TextField(blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.room_type}"

class FoodOrder(models.Model):
    # --- Status Fields ---
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Ready for Pickup', 'Ready for Pickup'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    customer_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    order_date = models.DateField()
    order_time = models.TimeField()
    ordered_items = models.JSONField() 
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    special_instructions = models.TextField(blank=True, null=True)
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.customer_name} on {self.order_date}"