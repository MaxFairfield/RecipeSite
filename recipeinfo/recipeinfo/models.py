from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
	name = models.CharField(max_length=100)
	parent_category = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)
	can_use_as_tag = models.BooleanField(default=True)

	def get_parents_display(self):
		if self.parent_category:
			return f"{self.parent_category.get_parents_display()} / {self.name}"
		return self.name

	def get_full_name(self):
		return self.get_parents_display()

	def __str__(self):
		return self.get_full_name()

class Recipe(models.Model):
	title = models.CharField(max_length=300)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	categories = models.ManyToManyField(Category)
	image = models.ImageField(upload_to='recipeinfo/static/', null=True, blank=True)
	ingredients = models.TextField()
	directions = models.TextField()
	prep_time = models.IntegerField(default=10)
	cook_time = models.IntegerField(default=10)
	created_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)], null=True, blank=True)

	def filename(self):
		return os.path.basename(self.image.name)

	def __str__(self):
		return self.title

class Review(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.recipe.title} - {self.user.username}"

class Feedback(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text