from django.shortcuts import render
from django.http import HttpResponse
from .models import course, judgement_system


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
        q = request.POST['q']
        if not q:
            return render(request, 'search_from.html', {'error': True})
        courses = course.objects.filter(name__contains=q)
        text = {}
        for course_s in courses:
            judges = judgement_system.objects.filter(course_id=course_s.id)
            text[course_s.id] = judges
        return render(request, 'search_result.html', {'courses': courses, 'query': q, 'judgement': text})

    else:
        return render(request, 'search_from.html', {'error': True})


def judgement(request, p1):
    judges = judgement_system.objects.filter(course_id=p1)
    return render(request, 'judgement.html', {'judgement': judges})


def add_judgement(request):
    info = request.params['data']

    # 从请求消息中 获取要添加评论的信息
    # 并且插入到数据库中
    # 返回值 就是插入使得否正确
    record = judgement_system.objects.create(name=info['name'],
                                             course=['course'],
                                             mark=info['mark'],
                                             time_for_homework=info['time_for_homework'],
                                             the_constitution_of_grade=info['the_constitution_of_grade'],
                                             comment_of_the_course=info['comment_of_the_course'],
                                             comment_of_the_teacher=info['comment_of_the_teacher'])

    return render(request, {'ret': 0})  # 注意，还没有添加HTML文件
