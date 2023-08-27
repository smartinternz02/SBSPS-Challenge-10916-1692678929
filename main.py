# main.py (for demonstration purposes only)

from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse

# models.py
class CustomUser(AbstractUser):
    # Add custom fields if needed (e.g., user_type)
    pass

# forms.py
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

# views.py
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

# urls.py
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
]

