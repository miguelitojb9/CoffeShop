"""
This class defines a Django form for handling user input and validation.

Attributes:
    Meta (class): A nested class that specifies metadata options for the form,
    such as the model it is associated with and the fields to include.
    fields (list): A list of fields that will be included in the form.
    widgets (dict, optional): A dictionary specifying custom widgets for form
    fields.
    labels (dict, optional): A dictionary mapping field names to custom labels.
    help_texts (dict, optional): A dictionary providing additional help text
    for form fields.
    error_messages (dict, optional): A dictionary defining custom error
    messages for form validation.

Methods:
    __init__(self, *args, **kwargs): Initializes the form instance,
    allowing for customization of fields or behavior during instantiation.
"""
from django import forms
from .models import Product


class ProductForm1(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name')
    description = forms.CharField(widget=forms.Textarea, label='Product Description')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Product Price')
    available = forms.BooleanField(required=False, label='Is Available')
    photo = forms.ImageField(required=False, label='Product Photo')
    
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
        )


class ProductForm(forms.ModelForm):
    """
    ProductForm is a Django ModelForm for creating and updating Product
    instances.
    This form provides custom widgets, labels, help texts, and error messages
    for the fields
    'name', 'description', 'price', 'available', and 'photo'.
    Attributes:
        Meta:
            model (Model): The model associated with this form (Product).
            fields (list): The fields to include in the form.
            widgets (dict): Custom widgets for rendering form fields.
            labels (dict): Custom labels for form fields.
            help_texts (dict): Help texts for form fields.
            error_messages (dict): Custom error messages for form validation.
    Methods:
        __init__(*args, **kwargs):
            Initializes the form and allows for additional customization.
    """
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
            'available': 'Is Available',
            'photo': 'Product Photo',
        }
        help_texts = {
            'name': 'Enter the name of the product (max 100 characters).',
            'description': 'Provide a detailed description of the product.',
            'price': 'Set the price of the product.',
        }
        error_messages = {
            'name': {
                'max_length': 'The name is too long. Maximum 100 characters allowed.',
            },
            'price': {
                'invalid': 'Enter a valid price.',
            },
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)