from django.contrib import admin
from .models import Property

 proma-working-code

admin.site.register(Property)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'price', 'city', 'is_available', 'owner')
    list_filter = ('property_type', 'city', 'is_available')
    search_fields = ('title', 'address', 'description')
 main
