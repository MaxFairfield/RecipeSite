from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Recipe, Feedback
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Count
from django.utils import timezone


def home_page(request):
	categories = Category.objects.all().order_by('id')

	recipes = Recipe.objects.all()
	trending_recipes = []

	for recipe in recipes:
		feedbackObjects = Feedback.objects.filter(recipe=recipe)

		if len(feedbackObjects) > 0:
			average = 0

			print(recipe)
			
			for v in feedbackObjects:
				print(f'    {v.rating}')
				average = average + v.rating

			average = average / len(feedbackObjects)

			recipe.rating = average

			trending_recipes.append(recipe)
	
	trending_recipes = sorted(trending_recipes, key=lambda x: x.rating, reverse=True)[:3]

	return render(
		request,
		'home.html',
		{
			'categories': categories,
			'trending_recipes': trending_recipes
		}
	)

def browse_recipes(request, id):
	search_category = Category.objects.get(id=id)

	q = request.GET.get('q') if request.GET.get('q') is not None else ''

	recipes = None

	if not q:
		# not searching
		recipes = Recipe.objects.filter(
			categories=search_category
		)
	else:
		#searching
		recipes = Recipe.objects.filter(
			categories=search_category and
			Q(title__icontains=q)
		)

	categories = Category.objects.all().order_by('id')
	return render(
		request,
		'browse_recipes.html',
		{
			'search_category': search_category,
			'recipes': recipes,
			'categories': categories,
			'q': q
		}
	)

def recipe_page(request, id):
	recipe = Recipe.objects.get(id=id)

	ingredients = recipe.ingredients.split('\n')
	ingredients = [line for line in ingredients if line.strip()]

	directions = recipe.directions.split('\n')
	directions = [line for line in directions if line.strip()]

	categories = Category.objects.all().order_by('id')

	feedback = Feedback.objects.filter(recipe=recipe)

	return render(
		request,
		'recipe_page.html',
		{
			'recipe': recipe,
			'ingredients': ingredients,
			'directions': directions,
			'rating': recipe.rating / 2 if recipe.rating is not None else None,
			'feedback': feedback,

			'categories': categories
		}
	)