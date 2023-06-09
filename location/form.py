
from django import forms
from .models import Apartment

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__' # Ou spécifier une liste de champs spécifiques

    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
