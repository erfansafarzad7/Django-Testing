from django.shortcuts import render, redirect
from django.views import View
from home.forms import UserRegisForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


class Home(View):
    def get(self, request):
        return render(request, 'home.home.html')


class About(View):
    def get(self, request, username):
        return render(request, 'home.about.html')


class UserRegisterView(View):
    form_class = UserRegisForm
    temp_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserRegisForm()
        return render(request, self.temp_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            try:
                User.objects.create_user(cd['username'], cd['email'], cd['password1'])
                messages.success(request, 'Registered Successfully !', 'success')
                return redirect('accounts:user_login')
            except IntegrityError as e:
                messages.warning(request, 'Username Already Exist !', 'warning')
                return render(request, self.temp_name, {'form': form})

        return render(request, self.temp_name, {'form': form})

