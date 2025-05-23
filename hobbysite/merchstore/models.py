from django.db import models
from django.urls import reverse
from profile.models import Profile


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
            related_name="owner"
            )
    description = models.TextField()
    price = models.DecimalField(max_digits=999999999, decimal_places=2)
    stock = models.IntegerField(default=0)
    status_choices = {
        'Out of Stock': 'NO_STOCK',
        'On Sale': 'SALE',
        'Available': 'STOCK',
    }
    status = models.CharField(
        max_length=255,
        choices=status_choices,
        default='AVAILABLE'
        )

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
        on_delete=models.SET_NULL,
        null=True,
        related_name="buyer"
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name="item"
        )
    amount = models.IntegerField()
    status_choices = {
        'On cart': 'CART',
        'To Pay': 'PAY',
        'To Ship': 'SHIPPING',
        'To Recieve': 'TRANSIT',
        'Delivered': 'DONE'
    }
    status = models.CharField(
        max_length=255,
        choices=status_choices,
        default='CART'
        )
    created_on = models.DateTimeField(auto_now_add=True)
