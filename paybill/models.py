from django.db import models
from django.contrib.auth.models import User
from enroll.models import ProductInfo
from django.core.validators import MaxValueValidator, MinValueValidator    

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

    # @property
    # def total_cost(self):
    #     return self.quantity * self.product.discounted_price




