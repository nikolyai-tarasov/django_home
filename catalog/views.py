
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm, ProductModeratorForm


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'



class ContactsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'contacts.html'


class IndexView(ListView):
    model = Product
    template_name = 'base.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'


class FormCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'forms.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)





class ReformUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'reform.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user != self.object.owner:
            raise PermissionDenied

        self.object.save()
        return self.object

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        elif user == self.object.owner:
            return ProductForm
        raise PermissionDenied







class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if   self.request.user.has_perm('catalog.can_delete_product') or  self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied


