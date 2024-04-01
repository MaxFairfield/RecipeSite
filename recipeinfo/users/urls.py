from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LoginView
from django.views.generic import RedirectView
from users import views as users_views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('create-recipe/', views.create_recipe_view, name='create_recipe'),

    #reset password
    path('', include('django.contrib.auth.urls')),
    path('reset/done/', users_views.custom_password_reset_done, name='password_reset_done'),
]
