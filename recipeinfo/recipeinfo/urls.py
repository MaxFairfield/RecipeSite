from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('browse-recipes/<int:id>/', views.browse_recipes, name='browse_recipes'),
    path('recipe/<int:id>/', views.recipe_page, name='recipe_page'),

    path('users/', include('users.urls')),
]
