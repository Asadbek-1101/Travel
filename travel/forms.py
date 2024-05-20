from django import forms
from .models import Categories, Davlatlar

class CreateDavlat(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    categories = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )
    class Meta:
        model = Davlatlar
        fields = ('name', 'price', 'categories', 'image')