from django.core.management.base import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        cat_1 = Category.objects.create(name="Овощи", description="Плодовые")

        products = [
            {'name':'Томат','description':'Обычный','category':cat_1,'price':123,
             'created_at':'2024-10-18','updated_at':'2024-10-18'},
            {'name': 'Баклажан', 'description': 'Обычный', 'category': cat_1, 'price': 213,
             'created_at': '2024-10-18', 'updated_at': '2024-10-18'}
        ]
        for i in products:
            prod, created = Product.objects.get_or_create(**products)
            if created:
                self.stdout.write(self.style.SECCESS(f'Successfull added product: {prod.name}'))
            else:
                self.stdout.write(self.style.SECCESS(f'Product already exist: {prod.name}'))

