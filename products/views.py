"""
This module defines views for the products app in the CoffeeShop project.
"""

from django.views import generic
from django.urls import reverse_lazy
from products.forms import ProductForm1
from .models import Product


class ProductListView(generic.FormView):
    """
    ProductListView is a class-based view that handles the display of
    the product list page.
    Attributes:
        template_name (str): The path to the HTML template used to render
        the product list page.
    Methods:
        get(request, *args, **kwargs):
            Handles GET requests and renders the product list page using
            the specified template.
    """
    template_name = 'products/product_list.html'
    form_class = ProductForm1
    success_url = reverse_lazy('products:product_list')
    extra_context = {'obj': Product.objects.all()}
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)