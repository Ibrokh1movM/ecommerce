from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from django.core.mail import send_mail
from user.forms import LoginForm
from config.settings import DEFAULT_FROM_EMAIL


# Create your views here.


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('ecommerce:index')
            else:
                messages.add_message(request,
                                     messages.ERROR,
                                     'Invalid login')
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('ecommerce:index')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            get_name_by_email = user.email.split('@')[0]
            user.set_password(form.cleaned_data['password1'])
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            send_mail(
                f'{get_name_by_email}',
                'You successfully registered',
                DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False
            )
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('ecommerce:index')
        else:
            messages.error(request, "Registration failed. Please check your input.")
    else:
        form = RegisterForm()

    return render(request, "user/register.html", {"form": form})
