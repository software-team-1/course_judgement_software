from django.urls import path, include
from . import views
app_name = 'my_account'
urlpatterns = [
    path('', views.my_account),
    path('modify_judgement/', views.modify_judgement),

]
