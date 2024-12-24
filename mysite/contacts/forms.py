from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Seu Nome', max_length=100)