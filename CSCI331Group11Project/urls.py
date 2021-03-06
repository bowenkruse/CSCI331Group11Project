"""CSCI331Group11Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Profile import views as profile_views
from Message import views as message_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', profile_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Profile/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='Profile/logout.html'), name='logout'),
    path('', profile_views.home, name='home'),
    path('editprofile/', profile_views.edit_profile, name='editprofile'),
    path('search/', profile_views.search_for, name='search'),
    path('viewuser/', profile_views.view_profile, name='viewuser'),
    path('viewcourse/', profile_views.view_course, name='viewcourse'),
    path('addcourse/', profile_views.add_course, name='addcourse'),
    path('ajax/apply_rating/', profile_views.apply_rating, name='apply_rating'),
    path('ajax/send_message/', message_views.send_message, name='send_message'),
    path('messages/', message_views.message_user, name='message_user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


