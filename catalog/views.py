

from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm, ProductModeratorForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from .services import ProductServices


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset

class CategoryListView(ListView):
    model = Product
    template_name = 'category_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return ProductServices.products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = get_object_or_404(Category, id=category_id)
        return context



class ContactsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'contacts.html'


class IndexView(ListView):
    model = Product
    template_name = 'base.html'

@method_decorator(cache_page(60 * 15), name='dispatch')
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


