from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ("Audi", "Audi"),
    ("BMW", "BMW"),
    ("Bugatti", "Bugatti"),
    ("Mercedes", "Mercedes"),
    ("Range Rover", "Range Rover"),
    
)

# product details
class ProductInfo(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    product_image = models.ImageField(upload_to="CarImages")
    
    



