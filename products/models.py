"""
This module defines the Product model for the CoffeeShop application.

"""
from django.db import models


class Product(models.Model):
    """
    Product model represents an item available in the coffee shop.
    Attributes:
        name (str): The name of the product, limited to 100 characters.
        description (str): A detailed description of the product.
        price (Decimal): The price of the product with up to 10 digits
        and 2 decimal places.
        available (bool): Indicates whether the product is currently available.
        Defaults to True.
        photo (ImageField): An optional image of the product,
        stored in 'products/photos/'.
    Methods:
        __str__(): Returns the string representation of the product,
        which is its name.
    """
    
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(max_length=200, verbose_name='Description')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price'
    )
    available = models.BooleanField(default=True, verbose_name='Available')
    photo = models.ImageField(
        upload_to='products/photos/',
        verbose_name='Photo',
        null=True, blank=True,
    )

    def __str__(self):
        return f'{self.name}'
