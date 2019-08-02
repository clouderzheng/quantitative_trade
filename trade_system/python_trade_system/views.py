from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from python_trade_system.system import system_user_service
import json
import uuid
# Create your views here.

"""跳转首页"""
def index(request):
    return render(request, "index.html")

"""跳转登陆页面"""
def login(request):
    return render(request, "login.html")

"""登陆验证"""
@csrf_exempt
def loginin(request):
    # 获取参数
    account = request.POST.get("account")
    password = request.POST.get("password")

    result = {}
    user = system_user_service.get_system_user(account)

    if((user !=  False)):
        _password = user['password'].decode(encoding='utf-8')
        if(password == _password):
            result['code'] = '0000'
            result['msg'] = 'success'
            token = str(uuid.uuid1())
            result['token'] = token
            request.session[token] = str(user)
            return HttpResponse(json.dumps(result))

    result['code'] = '9999'
    result['msg'] = 'fail'
    return HttpResponse(json.dumps(result))

