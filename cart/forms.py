from django import forms
from onlineshop.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 51)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
