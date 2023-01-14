from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['name']
        last_name = request.POST['surname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            new_user = User.objects.create_user(username=username,
                                                email=email,
                                                password=pass1,
                                                first_name=first_name,
                                                last_name=last_name)
            new_user.save()
            return redirect("signin")

    return render(request, "auth/signup.html", {})


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Bad credentials")
            return redirect("signin")

    return render(request, "auth/signin.html", {})


def sign_out(request):
    logout(request)
    return redirect("/")
