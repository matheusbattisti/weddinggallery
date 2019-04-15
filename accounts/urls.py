from django.contrib.auth import views
from django.urls import path

from . import views as customViews

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', customViews.RegisterView.as_view(), name='register'),
]