from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, IndexView, ProductDetailView, FormCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('index/', IndexView.as_view(), name='index'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('forms/', FormCreateView.as_view(), name='forms'),
]