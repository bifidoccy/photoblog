from django.shortcuts import render
from contact.models import *
from django.views import View
from django.views.generic import CreateView
from .models import ContactModel
from .forms import ContactForm


class ContactView(View):
	def get(self, request):
		embed_map = EmbedMap.objects.last()
		form = ContactForm()
		return render(request, 'contact/contact.html', context={'map': embed_map.source, 'form': form})

class CreateComment(CreateView):
	model = ContactModel
	form_class = ContactForm
	success_url = '/'