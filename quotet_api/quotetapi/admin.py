from django.contrib import admin

from .models import Category, Item, Contact, HomepageInfo, Event

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Contact)
admin.site.register(HomepageInfo)
admin.site.register(Event)
admin.site.site_header = "Quotet Handmade Producers Admin"
admin.site.site_title = "Quotet Admin Portal"
admin.site.index_title = "Welcome to Quotet Handmade Producers Portal"
admin.site.site_url = "https://www.quotet.co.ke"