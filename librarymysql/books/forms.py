

from django import forms

from books.models import Book

class AddbooksForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'

# class AddbooksForm(forms.Form):
#     title = forms.CharField()
#     author = forms.CharField()
#     price = forms.IntegerField()
#     pages = forms.IntegerField()
#     language = forms.CharField()

