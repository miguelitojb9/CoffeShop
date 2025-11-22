from django.urls import path
from .views import OrderDetailView

urlpatterns = [
    path('mi-order/', OrderDetailView.as_view(), name='order_detail'),

]