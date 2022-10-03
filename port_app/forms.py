from cProfile import label
from dataclasses import fields
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': 'Name',
            'email': 'Email',
            'message': 'Your message',
        }
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'message': forms.TextInput(attrs={"class": "form-control"})
        }
