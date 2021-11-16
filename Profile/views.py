from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddCourseForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import UserProfile
from django.contrib import messages
from course.models import Course
from django.views.decorators.csrf import csrf_exempt

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
    all_profiles = UserProfile.objects.all()
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
    if 'q' in request.GET:
        query = request.GET.get('q', None)
        all_courses = Course.objects.all()
        if query:
            possible_course = all_courses.filter(title__exact=query)
        else:
            possible_course = None
        context = {
            'selectedCourse': possible_course,
            'form': AddCourseForm()
        }
        return render(request, 'Profile/viewCourse.html', context)


@login_required
def add_course(request):
    query = request.GET.get('w')
    current_user = request.user.userprofile
    selected_course = Course.objects.get(title=query)
    current_user.courses.add(selected_course)
    current_user.save()
    messages.success(request, "Course successfully added")
    return redirect('search')


@csrf_exempt
def apply_rating(request):
    rating = int(request.POST.get('given_rating', None))
    rated_user = request.POST.get('rated_user', None)
    rated_user_object = UserProfile.objects.get(slug__exact=rated_user)
    current_rating = rated_user_object.rating
    new_rating = (current_rating + rating) / 2
    rated_user_object.rating = new_rating
    rated_user_object.save()
    print(rated_user_object.rating)
    data = {
        'rating': new_rating
    }
    return JsonResponse(data)
