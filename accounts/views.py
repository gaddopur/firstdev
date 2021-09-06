from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from . import forms
from .tokens import account_activation_token
from articles.models import Article
from django.contrib import messages

CustomUser = get_user_model()

def signup_view(request):
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.is_active = False
            user.save()

            # verification mailing
            current_site = get_current_site(request)
            mail_subject = "Activate you internviews helper account"
            message = render_to_string('accounts/activate.html', {
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('<h1>Please confirm your email address to complete the registration.Please check your spam folder also.If you did not recieve mail please contact </h1>')
    else :
        user_form = forms.UserForm()
    return render(request, 'accounts/signup_view.html',
          {
             'user_form' : user_form,
          })

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(user.get_absolute_url())
    else:
        return HttpResponse('Activation link is invalid!')

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
                return redirect(user.get_absolute_url())
        else:
            messages.error(request, "Please enter valid email and passaword")

    else:
        form = AuthenticationForm()
    return render(request, "accounts/login_view.html", {'form': form})

@login_required(login_url = "accounts:login")
def logout_views(request):
    prev = request.META.get('HTTP_REFERER')
    logout(request)
    messages.success(request, "You logged out")
    return redirect(prev)

@login_required(login_url = "accounts:login")
def profile_views(request, email):
    user = CustomUser.objects.get(email=email)
    articles = Article.objects.filter(author=user).order_by('date')
    return render(request, "accounts/profile.html",
            {
                'profile': user,
                'articles': articles
            }
    )

def userRecovery(request):
    if not request.user.is_anonymous:
        return redirect(request.user.get_absolute_url())
    if request.method == "POST":
        form = forms.PasswordResetForm(data=request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['email']
            current_site = get_current_site(request)
            mail_subject = "Change your password"
            user = CustomUser.objects.get(email=to_email)
            message = render_to_string('accounts/activate.html', {
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'recovery': True,
            })
            # from_email = EMAIL_HOST_USER
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('We have sent recovery letter to your registered email')

    else:
        form = forms.PasswordResetForm()
    return render(request, 'accounts/recovery.html', {'form': form})


def userNewpassword(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if request.method == "POST":
            form = forms.PasswordUpdateForm(data=request.POST, user=user)
            if form.is_valid():
                user = form.save()
                user.save()
                login(request, user)
                return redirect(user.get_absolute_url())
        else:
            form = forms.PasswordUpdateForm(data=request.POST, user=user)
        return render(request, 'accounts/newpassword.html', {'form': form})

    else:
        return HttpResponse('Recovery link is invalid!')