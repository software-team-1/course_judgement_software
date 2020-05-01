from django.shortcuts import render
from course_search_judgement.models import course, judgement_system


def my_account(request):
    user = request.user
    judges = judgement_system.objects.filter(name_id=user.id)
    for judge in judges:
        my_course = course.objects.filter(id=judge.course_id)
        judge.course_name = my_course[0].name
        judge.course_teacher = my_course[0].teacher
    return render(request, 'my_account.html', {'my_account': judges})
