from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIVISION_CHOICES = (
    ("Dhaka", "Dhaka"),
    ("Chattogram", "Chattogram"),
    ("Rajshahi", "Rajshahi"),
    ("Sylhet", "Sylhet"),
    ("Rangpur", "Rangpur"),
    ("Khulna", "Khulna"),
    ("Mymensingh", "Mymensingh"),
    ("Barisal", "Barisal"),
)


# customer details
class CustomerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=30)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    area = models.TextField()
    
    def __str__(self):
        return str(self.id)



