from django.db import models
from django.urls import reverse


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
    description = models.TextField()
    price = models.DecimalField(max_digits=999999999, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ['name', 'product_type', 'description', 'price']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('merchstore:itempage', args=[self.pk])
