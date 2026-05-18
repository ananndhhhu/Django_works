

from django import forms

from users.models import Employee

class AddnewForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'


