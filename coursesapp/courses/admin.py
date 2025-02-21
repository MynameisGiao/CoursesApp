from django.contrib import admin
from .models import Category, Courses
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id','name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Courses)
