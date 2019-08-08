from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from python_trade_system.system import system_user_service
import json
import uuid
from python_trade_system.jq_util.get_international_indice import InternationalIndice
from python_trade_system.system.date_format_util import DateEnconding
import numpy as np
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

"""获取纳克达斯指数"""
@csrf_exempt
def get_Nasdaq_Composite_Index(request):

    try:
        internationalIndice = InternationalIndice()
        data = internationalIndice.get_Nasdaq_Composite_Index(100)
        times = np.array( data['day']).tolist()
        view_data = np.array(data[['open','close','low','high']]).tolist()
        code_name = data['name'][0]
        result = {"times" : times, "view_data" : view_data,"code_name" : code_name}
    except:
        result['code'] = "9999"
        result.msg = "获取国际指数失败"
    else:
        result['code'] = "0000"
    return HttpResponse(json.dumps(result, cls=DateEnconding))

