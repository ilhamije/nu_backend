from django.contrib import admin
from .models import Lapak

class LapakAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'picture1',
                    'picture2',
                    'picture3',
                    'city',
                    'address',
                    'related_url',
                    'latitude',
                    'longitude',
                    'additional_info']

admin.site.register(Lapak, LapakAdmin)