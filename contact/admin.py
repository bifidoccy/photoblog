from django.contrib import admin
from contact.models import *


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'subject']

admin.site.register(About)
admin.site.register(OurPhilosophy)
admin.site.register(EmbedMap)
admin.site.register(Social)