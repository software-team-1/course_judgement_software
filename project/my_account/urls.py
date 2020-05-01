from django.urls import path, include
from . import views
app_name = 'my_account'
urlpatterns = [
    path('my_account', views.my_account),
]
