from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

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

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('Cash', 'Cash'),
            ('Card', 'Card'),
            ('Mobile Banking', 'Mobile Banking'),
        ],
        default='Cash'
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Paid', 'Paid'),
            ('Failed', 'Failed'),
        ],
        default='Pending'
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Payment - {self.booking.user.username}"