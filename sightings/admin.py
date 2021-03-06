from django.contrib import admin
from .models import Sighting

# Register your models here.
class SightingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['talent']}),
        (None,               {'fields': ['location']}),
    ]
    list_display = ('talent', 'author', 'location', 'datetime')
    def save_model(self, request, obj, form, change):
    	obj.author = request.user
        obj.save()

admin.site.register(Sighting, SightingAdmin)