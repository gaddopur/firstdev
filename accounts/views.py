from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Profile
from articles.models import Article
from django.contrib import messages

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
            print("Hello Signup")
            print(profile.first_name)
            login(request, user)
            messages.success(request, "You Signup successfully")
            return render(request, 'accounts/profile.html', {'profile':profile})
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
            messages.success(request, "You logged in successfully")
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("articles:articles_list")
        else:
            messages.error(request, "Please enter valid username and passaword")

    else:
        form = AuthenticationForm()
    return render(request, "accounts/login_view.html", {'form': form})

def logout_views(request):
    prev = request.META.get('HTTP_REFERER')
    logout(request)
    messages.success(request, "You logged out")
    return redirect(prev)
    # return redirect("articles:articles_list")

# @login_required(login_url = "/accounts/login")
def profile_views(request, username):
    user =  User.objects.get(username=username)
    articles = Article.objects.filter(author=user).order_by('date')
    profile = Profile.objects.get(user=user)
    return render(request, "accounts/profile.html",
            {
                'profile': profile,
                'articles': articles
            }
    )
