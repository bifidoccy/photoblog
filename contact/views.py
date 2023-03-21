from django.shortcuts import render
from contact.models import *
from django.views import View
from django.views.generic import CreateView
from .models import ContactModel
from .forms import ContactForm


class ContactView(View):
	def get(self, request):
		embed_map = EmbedMap.objects.last()
		context = {'form': ContactForm()}
		if embed_map is not None:
			context['map'] = embed_map.source 
		return render(request, 'contact/contact.html', context=context)

class CreateComment(CreateView):
	model = ContactModel
	form_class = ContactForm
	success_url = '/'