from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Profile

def signup_view(request):
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        profile_form = forms.ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            user.save()
            profile.save()
            login(request, user)
            return render(request, 'accounts/profile.html', {'Profile':profile})
    else :
        user_form = forms.UserForm()
        profile_form = forms.ProfileForm()
    return render(request, 'accounts/signup_view.html',
          {
             'user_form' : user_form,
             'profile_form' : profile_form
          })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if(form.is_valid()):
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("articles:articles_list")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login_view.html", {'form':form})

def logout_views(request):
    if request.method == "POST":
        logout(request)
        return redirect("articles:articles_list")

# @login_required(login_url = "/accounts/login")
def profile_views(request, username):
    user =  User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, "accounts/profile.html", {'Profile':profile})
