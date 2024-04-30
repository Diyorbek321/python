from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.custom_login, name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
]
