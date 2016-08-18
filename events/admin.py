from django.contrib import admin

from .models import Collection, Phase, Memory

admin.site.register(Collection)
admin.site.register(Phase)
admin.site.register(Memory)