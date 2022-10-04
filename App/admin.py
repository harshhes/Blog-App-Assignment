from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','author', 'created_at', 'updated_at']


# admin.site.register(Blog)
