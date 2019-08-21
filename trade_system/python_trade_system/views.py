from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from python_trade_system.system import system_user_service
import json
import uuid
from python_trade_system.system.date_format_util import DateEnconding
# Create your views here.
from python_trade_system.jq_service import get_index_service
import traceback
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
def get_Global_Index(request):

    try:
        result = {}
        """获取纳斯达克指数信息"""
        get_index_service.get_NASDAQ_index(result)
        get_index_service.get_SSE_50_index(result)
    except:
        traceback.print_exc()
        result['code'] = "9999"
        result['msg'] = "获取国际指数失败"

    else:
        result['code'] = "0000"
    return HttpResponse(json.dumps(result, cls=DateEnconding))



"""跳转分析数据页面"""
@csrf_exempt
def stock_analyze_page(request):
    return render(request, "ui-alerts.html")