from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
try:

    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):

        if request.path != '/login/' and request.path != '/loginin/' and not  request.path.endswith("html"):
            # 参数token
            token = request.GET.get("token")
            # 会话token
            user = request.session.get(token, None)
            if (None == user) :
                return HttpResponseRedirect('/login/')