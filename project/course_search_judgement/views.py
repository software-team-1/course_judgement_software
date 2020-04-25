from django.shortcuts import render
from django.http import HttpResponse
from .models import course

# Create your views here.


def search_from(request):
    return render(request, 'search_from.html')


def search_result(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        courses = course.objects.filter(name__contains=q)
        return render(request, 'search_result.html', {'courses': courses, 'query': q})

    else:
        return render(request, 'search_from.html', {'error': True})
