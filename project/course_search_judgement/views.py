from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import course, judgement_system, thumb_up
from log_sign.models import normal_user
from datetime import datetime


# Create your views here.


def search_from(request):
    return render(request, 'search_from.html')


def search_result(request):
    # if 'q' in request.GET and request.GET['q']:
    #     q = request.GET['q']
    #     courses = course.objects.filter(name__contains=q)
    #     return render(request, 'search_result.html', {'courses': courses, 'query': q})
    #
    # else:
    #     return render(request, 'search_from.html', {'error': True})

    if request.POST:
        q = request.POST.get('q') #q是搜索框里搜索的课程
        p = request.POST.get('p') #p是搜索框下方的给定分类
        r = request.POST.get('r')  # r为热门课程请求
        user = request.user
        user_ = normal_user.objects.filter(user=user)
        user_id = user_[0].id
        if (not q and not p and not r) or (r and q):  # 两种错误情况处理：搜索框没输入点击搜索/在搜索框输入后点“热门课程”，都会重新刷新页面
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
            return render(request, 'search_result.html', {'courses': courses, 'query': q, 'judgement': text})

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
            return render(request, 'search_result.html', {'courses': courses, 'query': p, 'judgement': text})

        if p and q:
            courses = course.objects.filter(name__contains=q, type__contains=p)
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
            return render(request, 'search_result.html', {'courses': courses, 'query': q, 'judgement': text})

        if r and not q:
            courses = course.objects.filter(judgement_system__number_of_thumb_up__gte=5).distinct()  #某门课有评论点赞数高于x即成为热门课程
            #judgement_system_obj = SysUser.objects.all().aggregate(Max('number_of_thumb_up'))
            #judgement_system_obj = judgement_system.objects.filter(number_of_thumb_up = 5)
            #courses = judgement_system_obj.course
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
            return render(request, 'search_result.html', {'courses': courses, 'query': r, 'judgement': text})

    else:
        return render(request, 'search_from.html', {'error': True})


def judgement(request, p1):
    judges = judgement_system.objects.filter(course_id=p1)
    return render(request, 'judgement.html', {'judgement': judges})


def judgement_for_course(request):
    return render(request, 'add_judgement.html')


def add_review(request, id):
    return render(request, 'add_review.html')


def judgement_for_thumb_up(request):
    return render(request, 'thumb_up.html')


def thumb(request):
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
    if request.method == "POST":
        comment_of_the_course = request.POST.get("comment_of_the_course")
        comment_of_the_teacher = request.POST.get("comment_of_the_teacher")
        the_constitution_of_grade = request.POST.get("the_constitution_of_grade ")
        time_for_homework = request.POST.get("time_for_homework")
        hard_core_mark = request.POST.get("hard_core_mark")
        recommend_mark = request.POST.get("recommend_mark")
        mark_of_interest = request.POST.get("mark_of_interest")
        course_id = request.POST.get("course_id")
        # q = request.POST.get("q")
        # p = request.POST.get("p")

        # judge = request.POST.get("id")
        # modify_judge = judgement_system.objects.filter(id=judge)
        # course_id = modify_judge[0].course_id
        # modify_judge.delete()
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
    # return render(request, 'search_result.html')
    return search_result(request)
    # return redirect("/search_result/")  # 注意，还没有添加HTML文件
