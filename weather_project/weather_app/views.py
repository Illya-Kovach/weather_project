from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
import requests

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('main')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    # Зробити логіку входу
    pass

def logout_view(request):
    # А тут виходу
    pass

def main_page(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        # Юзати ОпенВерезАпі, не забути
        # Збереження історії не забути
        weather_data = {
            'city': city,
            'temperature': '20',
            'description': 'Sunny'
        }
    return render(request, 'main.html', {'weather': weather_data})

def history(request):
    # Тут робити історію пошуку. Hier commt die Sonne!
    pass
