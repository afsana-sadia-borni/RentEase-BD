from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Property(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    # ম্যাপের জন্য координаты (Latitude & Longitude)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    rent = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    property_type = models.CharField(
        max_length=50,
        choices=[
            ('Apartment', 'Apartment'),
            ('House', 'House'),
            ('Room', 'Room'),
            ('Office', 'Office'),
            ('Shop', 'Shop'),
        ],
        default='Apartment'
    )

    is_available = models.BooleanField(default=True)

    description = models.TextField()

    image = models.ImageField(
        upload_to='properties/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Booking(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    booking_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.property.title}"



class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # bKash / Nagad নির্বাচন করার অপশন
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('bKash', 'bKash'),
            ('Nagad', 'Nagad'),
            ('Rocket', 'Rocket'),
            ('Cash', 'Cash'),
        ],
        default='bKash'
    )
    
    # পেমেন্ট পাঠানোর অ্যাকাউন্ট নম্বর
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Paid', 'Paid'),
            ('Failed', 'Failed'),
        ],
        default='Pending'
    )
    
    # ট্রানজেকশন আইডি (TrxID)
    transaction_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_method} Payment - {self.booking.user.username}"


class Profile(models.Model):
    ROLE_CHOICES = (
        ('tenant', 'Tenant (ভাড়াটিয়া)'),
        ('landlord', 'Landlord (বাড়িওয়ালা)'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='tenant')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
class Review(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.property.title} ({self.rating}★)"