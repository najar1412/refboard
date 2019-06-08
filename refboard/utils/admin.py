from django.contrib import admin

from .models import Thing, Thingy, RefMaterial

admin.site.register(Thing)
admin.site.register(Thingy)
admin.site.register(RefMaterial)