from django import forms
from django.core.exceptions import ValidationError

from .models import Product

forbidden_words = ['казино','криптовалюта','крипта','биржа','дешево','бесплатно','обман','полиция','радар']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','category','description','price','created_at',]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower() in forbidden_words:
            raise ValidationError(f'В имени использовано запрещенное слово {name}')
        return name

