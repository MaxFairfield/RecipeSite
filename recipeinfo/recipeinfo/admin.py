from django.contrib import admin
from .models import Category, Recipe, Feedback

admin.site.site_header = 'RecipeApp Admin'
admin.site.site_title = 'RecipeApp Admin Portal'
admin.site.index_title = 'RecipeApp Administration'

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Feedback)