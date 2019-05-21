from django.contrib import admin

# Register your models here.

from .models import Exhibit, Object

admin.site.register(Exhibit)
admin.site.register(Object)
