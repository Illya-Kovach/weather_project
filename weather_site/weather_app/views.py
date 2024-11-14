from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .models import SearchHistory
from django.contrib.auth import logout

def main(request):
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            api_key = settings.OPENWEATHER_API_KEY
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=uk'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description'],
                }
                if request.user.is_authenticated:
                    SearchHistory.objects.create(
                        user=request.user,
                        city=weather_data['city'],
                        temperature=weather_data['temperature'],
                        description=weather_data['description']
                    )
            else:
                messages.error(request, "Не вдалося знайти місто або сталася помилка.")
        else:
            messages.error(request, "Будь ласка, введіть назву міста.")

    return render(request, 'main.html', {'weather_data': weather_data})
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Аккаунт создан для {user.username}!')
            return redirect('main')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def index_page(request):
    return render(request, 'index.html')


def history(request):
    if request.user.is_authenticated:
        history = SearchHistory.objects.filter(user=request.user).order_by('-search_date')[:10]
    else:
        history = []

    return render(request, 'history.html', {
        'history': history
    })

