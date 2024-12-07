from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import lower
from users.models import CustomUser

from .models import Product

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'description', 'price', 'created_at', 'owner', ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['created_at'].widget.attrs.update({'class': 'form-control'})
        self.fields['owner'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')

        if name.lower() in forbidden_words:
            raise ValidationError(f'В имени использовано запрещенное слово {name}')
        elif description is not None:
            lower_ = description.lower()
            for i in forbidden_words:
                if i in lower_:
                    raise ValidationError(f'В описании использовано запрещенное слово {i}')

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if float(price) < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price






class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['publication_status', ]
