from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Recipe

def home_page(request):
	categories = Category.objects.all().order_by('id')
	return render(request, 'home.html', {'categories': categories})

def browse_recipes(request, id):
	search_category = Category.objects.get(id=id)

	recipes = Recipe.objects.filter(categories=search_category)
	categories = Category.objects.all().order_by('id')
	return render(
		request,
		'browse_recipes.html',
		{
			'search_category': search_category,
			'recipes': recipes,
			'categories': categories
		}
	)

def recipe_page(request, id):
	recipe = Recipe.objects.get(id=id)

	ingredients = recipe.ingredients.split('\n')
	ingredients = [line for line in ingredients if line.strip()]

	directions = recipe.directions.split('\n')
	directions = [line for line in directions if line.strip()]

	categories = Category.objects.all().order_by('id')

	return render(
		request,
		'recipe_page.html',
		{
			'recipe': recipe,
			'ingredients': ingredients,
			'directions': directions,
			'rating': recipe.rating / 2 if recipe.rating is not None else None,

			'categories': categories
		}
	)