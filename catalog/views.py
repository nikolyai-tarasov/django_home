from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactsView(ListView):
    model = Product
    template_name = 'contacts.html'


class IndexView(ListView):
    model = Product
    template_name = 'base.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class FormCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'forms.html'
    success_url = reverse_lazy('catalog:home')

class ReformUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'reform.html'
    success_url = reverse_lazy('catalog:home')

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('catalog:home')