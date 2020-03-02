
from django.urls import path
from apps.usuario import views

urlpatterns = [
	path('welcome', views.welcome),
	path('register', views.register),
	path('login',views.login),
	path('logout/',views.logout),
]