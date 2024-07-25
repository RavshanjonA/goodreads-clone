from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from book.forms import RegisterForm, LoginForm
from book.models import Users


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "book/register.html", context=context)

    def post(self, request):
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book:login")
        else:
            context = {
                "form": form
            }
            return render(request, "book/register.html", context=context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "book/login.html", context=context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {user.username}.")
                return redirect("home")
            else:
                messages.warning(request, "With given data user not found")
                return redirect("home")
