from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('products')
        

        messages.error(request, "Username or password not found")
        return redirect('user.signin')


    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Password not match")
            return redirect("user.register")

        if len(password) < 8:
            messages.error(request, "Atleast password have 8 digits of character and number.")
            return redirect("user.register")

        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, "Account has successfully created.")
        return redirect("user.signin")

        


    return render(request, 'register.html')