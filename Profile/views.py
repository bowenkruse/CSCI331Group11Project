from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

User = get_user_model()


# Create your views here.
@login_required()
def home(request):
    logged_in_user = request.user.userprofile
    you = logged_in_user.user
    context = {
        'u': you,
    }
    return render(request, "Profile/profile.html", context)


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


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'Profile/edit_profile.html', context)
