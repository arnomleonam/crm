from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout as django_logout, login as app_login
from django.contrib import messages

def login(request):
    return render(request, "login.html")

def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            app_login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário/Senha inválido. Por favor, tente novamente.")
    return redirect("login")

def logout(request):
    django_logout(request)
    return redirect("login")
