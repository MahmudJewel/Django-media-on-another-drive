from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ProductInfo


class ProductInfoForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'size': '15', "class": "form-control", "placeholder": "Product name"}))
    price = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'size': '15', "class": "form-control", "placeholder": "Product price"}))
    descriptions = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'size': '15', "class": "form-control", "placeholder": "Product descriptions"}))
    # img = forms.ImageField(required=False)
    class Meta:
        model = ProductInfo
        fields = ['name', 'price', 'descriptions', 'img']
