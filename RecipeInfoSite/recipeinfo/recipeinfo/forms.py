from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from recipeinfo.models import Recipe, Category, User

class RegisterForm(UserCreationForm):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': 'Username'
		})
		self.fields['email'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': 'example@email.com'
		})
		self.fields['password1'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': 'Password'
		})
		self.fields['password2'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': 'Confirm Password'
		})

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': 'Username'
		})
		self.fields['password'].widget.attrs.update({
			'class': 'form-control',
			'placeholder': 'Password'
		})

	class Meta:
		model = User
		fields = ['username', 'password']

class RecipeCreationForm(forms.ModelForm):
	subcategories = Category.objects.filter(parent_category__isnull=False)
	category_choices = [(category.id, category.name) for category in subcategories]
	
	categories = forms.MultipleChoiceField(choices=category_choices)

	class Meta:
		model = Recipe
		fields = (
			'title',
			'categories',
			'image',
			'ingredients',
			'directions',
			'prep_time',
			'cook_time'
		)