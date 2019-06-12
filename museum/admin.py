from django.contrib import admin

# Register your models here.

from .models import Exhibit, Object

# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')
# make_published.short_description = "Mark selected stories as published"
#
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     ordering = ['title']
#     actions = [make_published]


admin.site.register(Exhibit)
admin.site.register(Object)
