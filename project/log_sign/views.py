from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import normal_user_form
from .models import normal_user


def home(request):
    # 主界面函数
    if request.user.is_authenticated:
        return render(request, 'search_from.html')
    else:
        return render(request, 'home.html')


def log_in(request):
    # 登录函数
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'log_in.html', {'error': '用户名或密码不存在'})
        else:
            login(request, user)
            return render(request, 'search_from.html')
    else:
        return render(request, 'log_in.html')


def log_out(request):
    # 登出函数
    logout(request)
    return redirect("log_sign:home")


def register(request):
    # 注册功能函数
    if request.method == 'POST':
        register_forms = normal_user_form(request.POST)
        if register_forms.is_valid():
            register_forms.save()
            user = authenticate(username=register_forms.cleaned_data['username'],
                                password=register_forms.cleaned_data['password1'])
            user.email = register_forms.cleaned_data['email']
            normal_user(user=user, student_number=register_forms.cleaned_data['student_number'],
                        phone=register_forms.cleaned_data['phone']).save()
            login(request, user)
            return redirect("log_sign:home")
        else:
            text = {'register_forms': register_forms}
            return render(request, 'register.html', text)
    else:
        register_forms = normal_user_form()
    text = {'register_forms': register_forms}
    return render(request, 'register.html', text)
