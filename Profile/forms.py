from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
	name = forms.CharField(max_length=120)

	class Meta:
		model = User
		fields = ['username', 'name', 'password1', 'password2']

		widget = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'password1': forms.TextInput(attrs={'class': 'form-control'}),
			'password2': forms.TextInput(attrs={'class': 'form-control'}),

		}

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['name', 'bio', 'image']


class AddCourseForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['courses']


