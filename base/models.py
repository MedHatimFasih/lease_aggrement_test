from django.db import models
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
    

class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])
    
class City(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    


class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_guests = models.IntegerField()
    relationship = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    id_card_or_passport = models.CharField(max_length=100)
    guest_names = models.TextField()

    def __str__(self):
        return f"Reservation for {self.property.title} from {self.start_date} to {self.end_date}"
    

    
