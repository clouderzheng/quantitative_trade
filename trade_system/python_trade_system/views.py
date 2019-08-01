from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import system_user_service
import json
# Create your views here.

def index(request):
    return HttpResponse("hello world")

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

    if((user !=  False) & (user['password'].decode(encoding='utf-8') == password)):
        result['code'] = '0000'
        result['msg'] = 'success'
    else:
        result['code'] = '9999'
        result['msg'] = 'fail'
    return HttpResponse(json.dumps(result))

