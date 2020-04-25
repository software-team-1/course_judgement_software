from django.urls import path
from . import views


urlpatterns = [
    path('search_from/', views.search_from),
    path('search_result/', views.search_result)  #结果查询显示页面
]