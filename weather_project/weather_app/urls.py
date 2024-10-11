from django.urls import path
from .views import register, login_view, logout_view, main_page, history

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', main_page, name='main'),
    path('history/', history, name='history'),
]
