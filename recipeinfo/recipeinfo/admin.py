from django.contrib import admin
from .models import Category, Recipe

admin.site.site_header = 'RecipeApp Admin'
admin.site.site_title = 'RecipeApp Admin Portal'
admin.site.index_title = 'RecipeApp Administration'

admin.site.register(Category)
admin.site.register(Recipe)