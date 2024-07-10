from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustumerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'date_created', 'active')
    list_filter = ('active', 'date_created')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    ordering = ['last_name', 'first_name']

# Register your models here.
