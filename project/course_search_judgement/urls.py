from django.urls import path
from . import views
app_name = 'course_search_judgement'

urlpatterns = [
    path('search_from/', views.search_from, name='search_from'),
    path('search_result/', views.search_result, name='search_result'),  #结果查询显示页面
    path('add_review/<int:id>/',views.add_review,name='add_review'),
    path('<int:p1>/', views.judgement),
    path('add_judgement/', views.judgement_for_course),  # 提交课程的评价结果
    path('add_judgement/submit', views.add_judgement),  # 提交课程的评价结果
    path('thumb_up/', views.judgement_for_thumb_up),  # 提交课程的评价结果
    path('thumb_up/submit', views.thumb_up_dealing)  # 提交课程的评价结果
]
