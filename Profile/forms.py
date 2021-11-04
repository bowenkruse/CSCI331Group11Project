from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
	name = forms.CharField(max_length=120)

	class Meta:
		model = User
		fields = ['username', 'name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['name', 'bio', 'image']
