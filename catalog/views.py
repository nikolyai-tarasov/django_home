from catalog.models import Product
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


# def home(request):
#     prod = Product.objects.all()
#     context = {"products": prod}
#     return render(request, "home.html", context)

class ContactsView(ListView):
    model = Product
    template_name = 'contacts.html'


# def contacts(request):
#     return render(request, "contacts.html")

class IndexView(ListView):
    model = Product
    template_name = 'base.html'


# def index(request):
#     return render(request, "base.html")

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


# def product_detail(request, prod_id):
#     prod = Product.objects.get(id=prod_id)
#     context = {"products": prod}
#     return render(request, "product_detail.html", context)