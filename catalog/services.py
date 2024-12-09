from .models import Product

class ProductServices:
    @staticmethod
    def products_by_category(category_id):
        return Product.objects.filter(category_id=category_id)