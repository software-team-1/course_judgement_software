from datetime import datetime

from django.shortcuts import render, redirect
from course_search_judgement.models import course, judgement_system
from log_sign.models import normal_user


def my_account(request):
    user = request.user
    user_ = normal_user.objects.filter(user=user)
    user_id = user_[0].id
    judges = judgement_system.objects.filter(name_id=user_id)
    for judge in judges:
        my_course = course.objects.filter(id=judge.course_id)
        judge.course_name = my_course[0].name
        judge.course_teacher = my_course[0].teacher
    return render(request, 'my_account.html', {'my_account': judges})


def modify_judgement(request):
    if request.method == "POST":
        comment_of_the_course = request.POST.get("comment_of_the_course")
        comment_of_the_teacher = request.POST.get("comment_of_the_teacher")
        the_constitution_of_grade = request.POST.get("the_constitution_of_grade ")
        time_for_homework = request.POST.get("time_for_homework")
        hard_core_mark = request.POST.get("hard_core_mark")
        recommend_mark = request.POST.get("recommend_mark")
        mark_of_interest = request.POST.get("mark_of_interest")
        judge = request.POST.get("id")
        modify_judge = judgement_system.objects.filter(id=judge)
        course_id = modify_judge[0].course_id
        modify_judge.delete()
        user = request.user
        user_ = normal_user.objects.filter(user=user)
        user_id = user_[0].id
        judgement_system(create_date=datetime.now(),
                         comment_of_the_course=comment_of_the_course,
                         comment_of_the_teacher=comment_of_the_teacher,
                         the_constitution_of_grade=the_constitution_of_grade,
                         time_for_homework=time_for_homework,
                         course_id=course_id,
                         hard_core_mark=hard_core_mark,
                         recommend_mark=recommend_mark,
                         mark_of_interest=mark_of_interest,
                         name_id=user_id).save()
    return redirect("/my_account/")


def delete(request):
    if request.method == "POST":
        judge = request.POST.get("id")
        delete_judge = judgement_system.objects.filter(id=judge)
        delete_judge.delete()
    return redirect("/my_account/")