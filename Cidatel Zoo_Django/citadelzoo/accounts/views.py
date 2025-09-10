from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def simple_login(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre','').strip()
        grado = request.POST.get('grado','').strip()
        if nombre and grado:
            username = f"{'{'}nombre{'}'}_{'{'}grado{'}'}".lower().replace(' ', '_')
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_unusable_password()
                user.first_name = nombre
                user.last_name = f"Grado {grado}"
                user.save()
            login(request, user)
            messages.success(request, f"¡Bienvenid@ {nombre}!")
            return redirect('home')
        messages.error(request, "Por favor escribe tu nombre y grado.")
    return render(request, 'accounts/login.html')

def simple_logout(request):
    logout(request)
    return redirect('home')
