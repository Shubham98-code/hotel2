from django.contrib import admin
from django.urls import path, include # <--- Make sure 'include' is imported
from . import views
urlpatterns = [
    
    # This enables URLs like /accounts/google/login/ and /accounts/confirm-email/
    path('accounts/', include('allauth.urls')),

    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('pre_order', views.pre_order, name='pre_order'),
    path('room', views.room, name='room'),
    path('room/', views.room_booking_view, name='room_booking'),
    path('pre-order/', views.pre_order_view, name='pre_order'),
    path('dashboard/', views.owner_dashboard_view, name='owner_dashboard'),
    path('order/<int:order_id>/update-status/', views.update_order_status,name='update_order_status'),
    path('booking/<int:booking_id>/update-status/',views.update_booking_status,name='update_booking_status'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('rooms', views.rooms, name='rooms'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
]