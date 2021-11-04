from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import ListView
from .models import UserProfile
from course.models import Course

User = get_user_model()


# Create your views here.
@login_required
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


@login_required
def search_for(request):
    query = request.GET.get('q', None)
    all_courses = Course.objects.all()
    all_profiles = UserProfile.objects.all()
    if query:
        possible_courses = all_courses.filter(title__icontains=query)
        possible_profiles = all_profiles.filter(name__icontains=query)

    else:
        possible_courses = None
        possible_profiles = None

    context = {
        'courses': possible_courses,
        'users': possible_profiles
    }

    if request.is_ajax():
        html = render_to_string(
            template_name="Profile/search-results-partial.html",
            context={"courses": possible_courses,
                     "users": possible_profiles}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'Profile/search.html', context)


@login_required
def view_profile(request):
    query = request.GET.get('q', None)
    print(query)
    all_profiles = UserProfile.objects.all()
    print(all_profiles)
    if query:
        possible_profile = all_profiles.filter(slug__exact=query)
    else:
        possible_profile = None
    context = {
        'selectedUser': possible_profile
    }
    return render(request, 'Profile/viewUser.html', context)


@login_required
def view_course(request):
    query = request.GET.get('q', None)
    all_courses = Course.objects.all()
    if query:
        possible_course = all_courses.filter(title__exact=query)
    else:
        possible_course = None
    context = {
        'selectedCourse': possible_course
    }
    return render(request, 'Profile/viewCourse.html', context)
