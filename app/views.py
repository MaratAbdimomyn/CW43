from distutils.command.clean import clean
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, ListView
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.views import View
from django.views.generic import TemplateView

class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        verify_url = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
        subject = 'Verify your email'
        message = f'Hello {user.username}, please click the link:\n\n{verify_url}'
        send_mail(subject, message, 'sender@example.com', [user.email])

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        user.is_active = False
        user.save()
        self.send_verification_email(user)
        return response

class Positive(TemplateView):
    template_name = 'positive.html'

class Negative(TemplateView):
    template_name = 'negative.html'

class VerifyEmailView(View):
    def get(self, request, user_pk, token):
        user = User.objects.get(pk=user_pk)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('positive')
        else:
            return redirect('negaitve')

class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class UserList(ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'users'