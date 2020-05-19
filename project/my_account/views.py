from datetime import datetime

from django.shortcuts import render, redirect
from course_search_judgement.models import course, judgement_system, thumb_up
from log_sign.models import normal_user
from django.contrib.auth.models import User


def my_account(request):
    user = request.user
    user_ = normal_user.objects.filter(user=user)
    user_id = user_[0].id
    judges = judgement_system.objects.filter(name_id=user_id)
    normal_user_ = normal_user.objects.filter(id=user_id)
    judges.student_number = normal_user_[0].student_number
    judges.phone = normal_user_[0].phone
    auth_ = User.objects.filter(id=normal_user_[0].user_id)
    judges.email = auth_[0].email
    judges.username = auth_[0].username
    for judge in judges:
        my_course = course.objects.filter(id=judge.course_id)
        judge.course_name = my_course[0].name
        judge.course_teacher = my_course[0].teacher
        judge.course_type = my_course[0].type
        judge.course_credit = my_course[0].credit
    for judge in judges:
        thumb_ = thumb_up.objects.filter(user_id_id=user_id, judgement_id_id=judge.id)
        if thumb_:
            judge.tb = 1
        else:
            judge.tb = 0
    return render(request, 'my_account.html', {'my_account': judges})


def thumb(request, p2):
    user = request.user
    user_ = normal_user.objects.filter(user=user)
    user_id = user_[0].id
    thumb_ = thumb_up.objects.filter(user_id_id=user_id, judgement_id_id=p2)
    if thumb_:
        judge = judgement_system.objects.get(id=p2)
        judge.number_of_thumb_up = judge.number_of_thumb_up - 1
        judge.save()
        thumb_ = thumb_up.objects.filter(judgement_id_id=p2, user_id_id=user_id)
        thumb_.delete()
    else:
        judge = judgement_system.objects.get(id=p2)
        judge.number_of_thumb_up = judge.number_of_thumb_up + 1
        judge.save()
        thumb_up(judgement_id_id=p2,
                 user_id_id=user_id).save()
    return redirect("/my_account/")


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
