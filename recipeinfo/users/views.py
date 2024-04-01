from django.shortcuts import render, redirect
from recipeinfo.forms import RegisterForm, LoginForm
from recipeinfo.forms import RecipeCreationForm
from django.contrib.auth import login, logout
from recipeinfo.models import Category
from django.urls import reverse

def register_view(request):
	categories = Category.objects.all().order_by('id')
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			login(request, form.save())
			return redirect('home')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form, 'categories': categories})

def login_view(request):
	categories = Category.objects.all().order_by('id')
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect('home')
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form, 'categories': categories})

def logout_view(request):
	logout(request)
	return redirect('home')

def profile_view(request):
	categories = Category.objects.all().order_by('id')
	if request.user.is_authenticated:
		return render(request, 'users/profile.html', {'categories': categories})
	else:
		return redirect('users:login')

def create_recipe_view(request):
	categories = Category.objects.all().order_by('id')
	if request.method == 'POST':
		form = RecipeCreationForm(request.POST, request.FILES)
		if form.is_valid():
			recipe = form.save(commit=False)

			#manually enter data
			recipe.author = request.user
			recipe.save() #save the recipe instance first

			selected_categories = form.cleaned_data['categories']
			categories = Category.objects.filter(id__in=selected_categories)
			parent_categories = categories.values_list('parent_category', flat=True).distinct()
			parent_categories_instances = Category.objects.filter(id__in=parent_categories)

			all_categories = categories | parent_categories_instances
			recipe.categories.set(all_categories)

			return redirect('home')
	else:
		form = RecipeCreationForm()
	return render(request, 'users/create_recipe.html', {'form': form, 'categories': categories})

def custom_password_reset_done(request):
    return redirect(reverse('users:login'))