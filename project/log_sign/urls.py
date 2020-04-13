from django.urls import path, include
from . import views
app_name = 'log_sign'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
]
