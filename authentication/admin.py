from django.contrib import admin
from .models import CustomerInfo

# Register your models here.
@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    # ordering field
    list_display = ['id', 'user', 'first_name', 'last_name', 'division', 'city', 'zipcode', 'area']



