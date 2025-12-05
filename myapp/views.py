from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render ,redirect, get_object_or_404
import datetime
import json # Import the json library
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.conf import settings  # <-- ADD THIS
import os                      # <-- ADD THIS
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from .models import RoomBooking, FoodOrder, ContactMessage # Updated imports
import json

# ... (all your other imports: render, redirect, EmailMessage, BytesIO, pisa, etc.) ...

def index(request):
    return render(request, 'index.html')
def pre_order(request):
    return render(request, 'pre-order.html')
def room(request):
    return render(request, 'room.html')
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def rooms(request):
    return render(request, 'rooms.html')

def register(request):
    if request.method == 'GET':
        # Just show the registration page
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        # Process the form data
        
        # Get data from the form
        # We use .get() to avoid errors if the field is missing
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # --- Server-Side Validation ---
        
        # 1. Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register') # 'register' is the name from urls.py

        # 2. Check if the user (email) already exists
        # We use email as the username for Django's User model
        if User.objects.filter(username=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return redirect('register')
        
        # 3. Create the new user
        try:
            # create_user handles password hashing automatically
            user = User.objects.create_user(
                username=email,  # Use email as the username
                email=email,
                password=password
            )
            
            # Add the full name (split into first and last)
            if full_name:
                names = full_name.split(' ', 1)
                user.first_name = names[0]
                if len(names) > 1:
                    user.last_name = names[1]
            
            user.save()
            
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login') # Send to login page after successful registration

        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('register')

def login_view(request):
    if request.method == 'GET':
        # Just show the login page
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        # Process the form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # We use the email as the username to authenticate
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Authentication was successful
            login(request, user)
            
            # Welcome message
            # Use first_name if available, otherwise the username (email)
            welcome_name = user.first_name if user.first_name else user.username
            messages.success(request, f'Welcome back, {welcome_name}!')
            
            # Redirect to the main 'home' page
            return redirect('home')
        else:
            # Authentication failed
            messages.error(request, 'Invalid email or password.')
            return redirect('login') # 'login' is the name from urls.py

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home') # Redirect to home page after logout



# --- Your existing views for login, register, etc. ---
# ... (keep them here) ...


# NEW VIEW for the room booking form
def room_booking_view(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        guests = request.POST.get('Guests')
        room_type = request.POST.get('RoomType')
        check_in = request.POST.get('CheckIn')
        check_out = request.POST.get('CheckOut')
        requests = request.POST.get('Requests')

        # --- Basic Server-Side Validation ---
        if not all([name, email, phone, guests, room_type, check_in, check_out]):
            messages.error(request, 'Please fill out all required fields.')
            return render(request, 'room.html') # Send user back to form

        try:
            # Compare dates
            check_in_date = datetime.date.fromisoformat(check_in)
            check_out_date = datetime.date.fromisoformat(check_out)

            if check_out_date <= check_in_date:
                messages.error(request, 'Check-out date must be after check-in date.')
                return render(request, 'room.html')
        
        except ValueError:
            messages.error(request, 'Invalid date format.')
            return render(request, 'room.html')
        # --- End Validation ---

        # Create and save the new booking
        booking = RoomBooking(
            name=name,
            email=email,
            phone=phone,
            guests=int(guests),
            room_type=room_type,
            check_in=check_in_date,
            check_out=check_out_date,
            requests=requests
        )
        booking.save()

        # Add a success message
        messages.success(request, 'Thank you! Your booking request has been submitted successfully.')
        return redirect('room_booking') # Redirect to the same page (or a 'thank you' page)

    # If it's a GET request (just loading the page), just render the template
    return render(request, 'room.html')



from django.core.mail import send_mail
from django.conf import settings # To get settings.EMAIL_HOST_USER

# ... (your other view functions: update_order_status, etc.) ...

# UPDATED: pre_order_view
def pre_order_view(request):
    if request.method == 'POST':
        # ... (all your existing code to get form data) ...
        customer_name = request.POST.get('customerName')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('customerEmail')
        preorder_date = request.POST.get('preorderDate')
        preorder_time = request.POST.get('preorderTime')
        special_instructions = request.POST.get('specialInstructions')
        ordered_items_json = request.POST.get('orderedItems')
        total_cost = request.POST.get('totalCost')

        # ... (your existing validation) ...
        
        try:
            ordered_items_data = json.loads(ordered_items_json)
            
            # Save the order (as you already do)
            order = FoodOrder(
                customer_name=customer_name,
                phone_number=phone_number,
                email=email,
                order_date=preorder_date,
                order_time=preorder_time,
                special_instructions=special_instructions,
                ordered_items=ordered_items_data,
                total_cost=float(total_cost)
            )
            order.save()

            messages.success(request, 'Your pre-order has been placed successfully!')
            
            # --- NEW: Send Confirmation Email ---
            if order.email: # Only send if they provided an email
                subject = 'Your Gupta Hotel Order is Confirmed!'
                message = f"""
Hi {order.customer_name},

Thank you for your pre-order! We have successfully received it.

Order ID: {order.id}
Pickup Time: {order.order_date} at {order.order_time}
Total Amount: ₹{order.total_cost}

We are prepering your order,please wait...

- The Gupta Hotel Team
"""
                try:
                    send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER, # From email
                        [order.email],             # To email
                        fail_silently=False,
                    )
                except Exception as e:
                    # Optional: Log the error if email fails
                    print(f"Error sending email: {e}")
            # --- End Email Logic ---

            return redirect('pre_order')

        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return render(request, 'pre-order.html')

    # If it's a GET request, just render the page
    return render(request, 'pre-order.html')

# ... (your other views like room_booking_view, pre_order_view) ...

@login_required # This secures the page
def owner_dashboard_view(request):
    # We only want to show this page to staff/superusers
    if not request.user.is_staff:
        # You can redirect them to the homepage
        return redirect('index') # Assumes you have a URL named 'index'

    # Get all bookings and orders, new ones first
    bookings = RoomBooking.objects.order_by('-booked_at')
    orders = FoodOrder.objects.order_by('-placed_at')

    context = {
        'bookings': bookings,
        'orders': orders,
    }
    return render(request, 'dashboard.html', context)

@login_required  # <-- 2. ADD THE DECORATOR
def pre_order(request):
    # This code will ONLY run if the user is logged in
    return render(request, 'pre-order.html')

@login_required  # <-- 2. ADD THE DECORATOR
def room_booking(request):
    # This code will ONLY run if the user is logged in
    # (You still need to create this view)
    return render(request, 'room_booking.html')

# ... (your existing views: room_booking_view, pre_order_view, owner_dashboard_view) ...

# myapp/views.py

# ... (your other imports and views) ...

# UPDATED: update_order_status
@login_required
def update_order_status(request, order_id):
    if not request.user.is_staff:
        return HttpResponseForbidden()

    if request.method == 'POST':
        order = get_object_or_404(FoodOrder, id=order_id)
        new_status = request.POST.get('new_status')
        
        # --- NEW: Check if status is changing TO Completed ---
        is_now_completed = new_status == 'Completed' and order.status != 'Completed'
        # --- End Check ---
        
        order.status = new_status
        order.save()
        
        messages.success(request, f"Order for {order.customer_name} updated to '{new_status}'.")

        # --- NEW: Send Invoice if just completed ---
        if is_now_completed and order.email:
            try:
                # 1. Create the PDF
                pdf_context = {'order': order}
                pdf_file = render_to_pdf('invoice_template.html', pdf_context)
                
                if pdf_file:
                    # 2. Create the email
                    subject = f"Your Gupta Hotel Order is Complete! (Invoice #{order.id})"
                    message = f"""
Hi {order.customer_name},

Your order (ID: {order.id}) is now complete and ready.
We have attached your final invoice for your records.

Thank you for choosing The Gupta Hotel!
"""
                    
                    email = EmailMessage(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER, # From
                        [order.email]             # To
                    )
                    
                    # 3. Attach the PDF
                    email.attach(
                        f'invoice_{order.id}.pdf', 
                        pdf_file, 
                        'application/pdf'
                    )
                    
                    # 4. Send
                    email.send()
                
                else:
                    messages.error(request, "Could not generate PDF for invoice.")
            
            except Exception as e:
                messages.error(request, f"Failed to send completion email: {e}")
        # --- End Invoice Logic ---

    return redirect('owner_dashboard')

@login_required
def update_booking_status(request, booking_id):
    # Only allow staff to access
    if not request.user.is_staff:
        return HttpResponseForbidden()

    if request.method == 'POST':
        # Find the specific booking
        booking = get_object_or_404(RoomBooking, id=booking_id)
        
        # Get the new status from the form
        new_status = request.POST.get('new_status')
        
        # Update and save
        booking.status = new_status
        booking.save()
        
        messages.success(request, f"Booking for {booking.name} updated to '{new_status}'.")
    
    # Redirect back to the dashboard
    return redirect('owner_dashboard')
# myapp/views.py

# ... (all your other imports) ...

# --- NEW IMPORTS for PDF and Email Attachments ---
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from io import BytesIO
from xhtml2pdf import pisa 

# --- NEW PDF HELPER FUNCTION ---
# --- UPDATED PDF HELPER FUNCTION (handles static files) ---
def render_to_pdf(template_src, context_dict={}):
    """
    Renders an HTML template into a PDF and returns the PDF content.
    Handles static files like images.
    """
    template = render_to_string(template_src, context_dict)
    result = BytesIO()

    # --- This is the new part: A callback to find static files ---
    def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute file system paths.
        """
        # uri will be /static/css/logo.png
        # We need to convert it to a file system path
        # settings.BASE_DIR points to your main project folder
        
        # Remove the leading slash
        sUrl = uri.lstrip('/') 
        
        # Join with the project's BASE_DIR
        path = os.path.join(settings.BASE_DIR, sUrl)

        # Make sure the file exists
        if not os.path.isfile(path):
            print(f"PDF Error: Could not find file {path}")
            return None
        
        return path
    # --- End of new part ---

    # Render the PDF, passing the new callback
    pdf = pisa.pisaDocument(
        BytesIO(template.encode("UTF-8")),
        result,
        link_callback=link_callback # <-- Pass the callback here
    )
    
    if not pdf.err:
        return result.getvalue()
    
    # If there's an error, print it to your console
    print(f"PDF Generation Error: {pdf.err}")
    return None
# --- NEW: Handle Contact Form Submission ---
@require_POST
@csrf_protect
def contact_submit(request):
    try:
        # Save to Database using request.POST (FormData)
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)