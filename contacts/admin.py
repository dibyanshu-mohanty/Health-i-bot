from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','contact_date')
    list_display_links=('name','email')
    search_fields=('name','contact_date')
    list_per_page=20

admin.site.register(Contact,ContactAdmin)