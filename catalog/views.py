from django.shortcuts import render
from catalog.models import Product


def home(request):
    prod = Product.objects.all()
    context = {"products": prod}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")


def index(request):
    return render(request, "base.html")


def product_detail(request, prod_id):
    prod = Product.objects.get(id=prod_id)
    context = {"products": prod}
    return render(request, "product_detail.html", context)
