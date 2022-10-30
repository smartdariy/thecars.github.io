from django import forms
from .models import *

class CommentForm(forms.Form):
    text = forms.CharField(
        label='comment',
        widget=forms.TextInput(attrs={'placeholder':'here'})
    )

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'