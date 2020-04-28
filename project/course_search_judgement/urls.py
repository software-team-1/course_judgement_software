from django.urls import path
from . import views
app_name = 'course_search_judgement'

urlpatterns = [
    path('search_from/', views.search_from, name='search_from'),
    path('search_result/', views.search_result, name='search_result')  #结果查询显示页面
]
