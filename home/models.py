from django.db import models


class Property(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='properties/', blank=True, null=True)

    def __str__(self):
        return self.title