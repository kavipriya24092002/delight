from django.forms import ModelForm
from.models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']
        
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
           
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message...',
                'rows': 3,
            }),
        }
            