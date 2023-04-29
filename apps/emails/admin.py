from django.contrib import admin
from apps.emails.models import *

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ( 'subject', 'body', 'created','status')
    list_editable = []

    #search_fields = ()
    list_per_page = 20





admin.site.register(Newsletter, NewsletterAdmin)

