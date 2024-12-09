from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, IndexView, ProductDetailView, FormCreateView, ReformUpdateView, \
    DeleteProductView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('index/', IndexView.as_view(), name='index'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('forms/', FormCreateView.as_view(), name='forms'),
    path('reform/<int:pk>/', ReformUpdateView.as_view(), name='reform'),
    path('delete_product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
path('category_list/<int:category_id>/', CategoryListView.as_view(), name='category_list'),
]
