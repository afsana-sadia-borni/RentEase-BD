from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('add-property/', views.add_property, name='add_property'),

    path('properties/', views.properties, name='properties'),

    path('property/<int:id>/', views.property_detail, name='property_detail'),


    # Authentication

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('profile/', views.profile, name='profile'),

    path('my-properties/', views.my_properties, name='my_properties'),

    path(
        'property/<int:id>/edit/',
        views.edit_property,
        name='edit_property'
    ),

    path(
        'property/<int:id>/delete/',
        views.delete_property,
        name='delete_property'
    ),

    path(
        'property/<int:id>/contact/',
        views.contact_owner,
        name='contact_owner'
    ),

    path(
        'property/<int:id>/book/',
        views.book_property,
        name='book_property'
    ),

    path(
        'my-bookings/',
        views.my_bookings,
        name='my_bookings'
    ),

    path(
        'owner-bookings/',
        views.owner_bookings,
        name='owner_bookings'
    ),

    path(
        'booking/<int:id>/confirm/',
        views.confirm_booking,
        name='confirm_booking'
    ),

    path(
        'booking/<int:id>/cancel/',
        views.cancel_booking,
        name='cancel_booking'
    ),

    path('logout/', views.user_logout, name='logout'),

]