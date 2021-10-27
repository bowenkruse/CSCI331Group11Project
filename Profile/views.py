from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

User = get_user_model()


# Create your views here.
def home(request):
    return render(request, "Profile/profile.html")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Profile/register.html', {'form': form})
