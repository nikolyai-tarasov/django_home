from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, index, product_all, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name='contacts'),
    path('index/', index, name='index'),
    path('product_all/', product_all, name='product_all'),
    path('product_detail/<int:prod_id>', product_detail, name='product_detail'),
]
