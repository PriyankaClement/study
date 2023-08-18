from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
