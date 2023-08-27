# listings/models.py
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# listings/views.py
from django.shortcuts import render
from .models import Product

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'products': products})
