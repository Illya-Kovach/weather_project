from .views import register, login_view, logout_view, index_page, history, main
from django.urls import path
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', index_page, name='index'),
    path('history/', history, name='history'),
    path('main/', main, name='main')
]


