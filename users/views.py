from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .models import Users
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, ProfileUpdateForm


class RegisterView(View):
    def get(self, request):
        register_form = UserForm()
        context = {
            'form': register_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        register_form = UserForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': register_form
            }
        return render(request, 'register.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(request, 'login.html', context=context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('bikes:home')
        context = {
            'form': login_form
        }
        return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('bikes:home')


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


class ProfileUpdate(View):
    def get(self, request):
        update_form = ProfileUpdateForm(instance=request.user)
        if update_form.is_valid():
            return redirect('users:profile')
        else:
            context = {
                'form': update_form
            }
            return render(request, 'profile_edit.html', context=context)

    def post(self, request):
        update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('users:profile')
        else:
            context = {
                'form': update_form
            }
            return render(request, 'profile_edit.html', context=context)
