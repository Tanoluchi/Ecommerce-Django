from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Campos que vamos a mostrar
    list_display = ['name', 'slug']\
    # Cuando se rellene campo 'name', automaticamente se rellenara el campo 'slug'
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Campos que vamos a mostrar
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    # Filtrar los productos
    list_filter = ['in_stock', 'is_active']
    # Campos editables
    list_editable = ['price', 'in_stock']