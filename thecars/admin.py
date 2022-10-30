from django.contrib import admin
from .models import *

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    list_filter = ('name', 'rating')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    list_filter = ('name', 'rating')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'year')}
    list_display = ('name', 'type', 'brand', 'year', 'price')
    list_filter = ('brand', 'type', 'rating')

@admin.register(UserAddon)
class UserAddonAdmin(admin.ModelAdmin):
    pass
