from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home_page, name='home'),
    path('browse-recipes/<int:id>/', views.browse_recipes, name='browse_recipes'),
    path('recipe/<int:id>/', views.recipe_page, name='recipe_page'),

    #inclusions
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)