import json

import django
from django.contrib.auth import authenticate
from django.http import JsonResponse

from authentication.forms import LoginForm
from enrollment.result import Result, Results


def login(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            login_form = LoginForm(json.loads(request.body.decode()))
        else:
            login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['user_name']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                django.contrib.auth.login(request, user)
                return JsonResponse(Result(data={"identity": user.identity}, data_message="登陆成功").to_dict())
            else:
                return JsonResponse(Result(data={}, data_message="用户名或密码错误,请重新登录", status=False).to_dict())
        else:
            return JsonResponse(Results.illegal_argument)


def index(request):
    if request.method == 'GET':
        # 提取浏览器中的cookie，如果不为空，表示已经登录
        user = request.user
        return JsonResponse(Result(data={"username": user.username}).to_dict())


def logout(request):
    if request.method == 'POST':
        django.contrib.auth.logout(request)
        return JsonResponse(Result(data_message='登出成功').to_dict())
