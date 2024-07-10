from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    area_code = models.CharField(max_length=3)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_phone(self):
        return f"({self.area_code}) {self.phone}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_city(self):
        return f"{self.city} - {self.state}"
    
    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})
    
    class Meta:
        db_table = "customer"
