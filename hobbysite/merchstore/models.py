from django.db import models
from django.urls import reverse
from user_management.models import Profile


# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
            ProductType,
            on_delete=models.SET_NULL,
            null=True,
            related_name="product"
            )
    owner = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            null=True,
            related_name="profile"
            )
    description = models.TextField()
    price = models.DecimalField(max_digits=999999999, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(max_length=255, choices={"Out of Stock", "On Sale", "Available"})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'product_type', 'description', 'price']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('merchstore:itempage', args=[self.pk])
    
class Transaction(models.Model):
    buyer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        related_name="profile"
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        related_name="product"
        )
    amount = models.IntegerField()
    status = models.CharField(max_length=255, choices={"On cart", "To Pay", "To Ship", "To Recieve", "Delivered"})
    created_on = models.DateTimeField(auto_now_add=True)
