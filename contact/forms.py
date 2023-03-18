from django import forms
from contact.models import *

class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactModel
		exclude = ['create_at']
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
			'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
			'message': forms.Textarea(attrs={'placeholder': 'Message'}),
		}