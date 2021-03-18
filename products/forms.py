from django import forms
from django.forms import ModelForm, Textarea
from django.forms.widgets import RadioSelect
from products.models import Products
from django.forms import ClearableFileInput, ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductsForm(forms.ModelForm):
    class Meta:
           model = Products
           fields = [
               'image',
               'gold_weight',
               'diamond_carat',
           ]