from django import forms
from .models import Personalinfo

class PersonalinfoForm(forms.ModelForm):

    class Meta:
        model = Personalinfo
        fields = ('first_name', 'last_name','email','phone','address','postalcode','city','country')


