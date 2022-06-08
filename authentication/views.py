import json

import django
from django.contrib.auth import authenticate

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
                request.session['id'] = user.id
                request.session['identity'] = user.identity
                return Result(data={"identity": user.identity}, data_message="登陆成功").to_response()
            else:
                return Result(data_message="登陆失败：用户名或密码错误,请重新登录", status=False).to_response()
        else:
            return Results.illegal_argument


def index(request):
    if request.method == 'GET':
        try:
            _id = request.session['id']
        except KeyError:
            return Results.not_login
        return Result(data={"user_id": _id}).to_response()


def logout(request):
    if request.method == 'POST':
        django.contrib.auth.logout(request)
        return Result(data_message='登出成功').to_response()
