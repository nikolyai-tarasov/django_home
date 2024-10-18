from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категории', help_text='Введите название категории')
    description = models.TextField(verbose_name='Введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', help_text='Введите газвание продукта')
    description = models.TextField('Введите описание продукта')
    image = models.ImageField(upload_to='product/photo', blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(verbose_name='Введите цену продукта')
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return f'{self.name} - {self.category}'

# Product.objects.create(name="Голубика",description="Темного цвета",category"Ягоды",price=450,created_at ="21-12-2023",updated_at="16-10-2024")