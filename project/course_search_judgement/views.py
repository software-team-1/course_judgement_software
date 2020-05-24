from django.shortcuts import render
from .models import course, judgement_system, thumb_up
from log_sign.models import normal_user
from datetime import datetime


def search_from(request):
    return render(request, 'search_from.html')


def search_result(request):
    # 返回搜索内容
    if request.POST:
        q = request.POST.get('q')  # q是搜索框里搜索的课程
        p = request.POST.get('p')  # p是搜索框下方的给定分类
        r = request.POST.get('r')  # r为热门课程请求
        user = request.user
        user_ = normal_user.objects.filter(user=user)
        user_id = user_[0].id
        if (not q and not p and not r) or (r and q) or (p and q):  # 两种错误情况处理：搜索框没输入点击搜索/在搜索框输入后点“热门课程”，都会重新刷新页面
            return render(request, 'search_from.html', {'error': True})
        if q and not p:
            courses = course.objects.filter(name__contains=q)
            text = {}
            for course_s in courses:
                judges = judgement_system.objects.filter(course_id=course_s.id)
                i = 1
                for judge in judges:
                    judge.judgement_id = i
                    i = i + 1
                    thumb_ = thumb_up.objects.filter(user_id_id=user_id, judgement_id_id=judge.id)
                    if thumb_:
                        judge.tb = 1
                    else:
                        judge.tb = 0
                text[course_s.id] = judges
            return render(request, 'search_result.html', {'mode': 1, 'courses': courses, 'query': q, 'judgement': text})
        if p and not q:
            courses = course.objects.filter(type__contains=p)
            text = {}
            for course_s in courses:
                judges = judgement_system.objects.filter(course_id=course_s.id)
                i = 1
                for judge in judges:
                    judge.judgement_id = i
                    i = i + 1
                    thumb_ = thumb_up.objects.filter(user_id_id=user_id, judgement_id_id=judge.id)
                    if thumb_:
                        judge.tb = 1
                    else:
                        judge.tb = 0
                text[course_s.id] = judges
            return render(request, 'search_result.html', {'mode': 2, 'courses': courses, 'query': p, 'judgement': text})
        if r and not q and not p:
            courses = course.objects.filter(
                judgement_system__number_of_thumb_up__gte=5).distinct()  # 某门课有评论点赞数高于x即成为热门课程
            text = {}
            for course_s in courses:
                judges = judgement_system.objects.filter(course_id=course_s.id)
                i = 1
                for judge in judges:
                    judge.judgement_id = i
                    i = i + 1
                    thumb_ = thumb_up.objects.filter(user_id_id=user_id, judgement_id_id=judge.id)
                    if thumb_:
                        judge.tb = 1
                    else:
                        judge.tb = 0
                text[course_s.id] = judges
            return render(request, 'search_result.html', {'mode': 3, 'courses': courses, 'query': r, 'judgement': text})

    else:
        return render(request, 'search_from.html', {'error': True})


def judgement(request, p1):
    judges = judgement_system.objects.filter(course_id=p1)
    return render(request, 'judgement.html', {'judgement': judges})


def thumb(request):
    # 点赞功能函数
    user = request.user
    user_ = normal_user.objects.filter(user=user)
    user_id = user_[0].id
    p2 = request.POST.get('judge_id')
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
    return search_result(request=request)


def add_judgement(request):
    # 添加评论函数
    if request.method == "POST":
        comment_of_the_course = request.POST.get("comment_of_the_course")
        comment_of_the_teacher = request.POST.get("comment_of_the_teacher")
        the_constitution_of_grade = request.POST.get("the_constitution_of_grade ")
        time_for_homework = request.POST.get("time_for_homework")
        hard_core_mark = request.POST.get("hard_core_mark")
        recommend_mark = request.POST.get("recommend_mark")
        mark_of_interest = request.POST.get("mark_of_interest")
        course_id = request.POST.get("course_id")
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
    return search_result(request)
