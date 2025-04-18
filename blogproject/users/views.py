from django.shortcuts import render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.urls import path

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        request.user.username = username
        request.user.email = email
        request.user.save()

        messages.success(request, 'Your profile has been updated!')
        return redirect('profile')

    return render(request, 'users/profile_update.html')


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='your_custom_path/login.html'), name='login'),
]

def login_view(request):
    return render(request, 'login.html')

