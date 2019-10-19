
from django.template import RequestContext
from django.shortcuts import render
from ..models.login.auth import modelLoginAuth
from ..models.common import modelCommon
from django.template import RequestContext

from django.shortcuts import redirect
def index(request):
        err_message = ""
        mail_address = request.POST.get("mail_address")
        login_auth = modelLoginAuth(request.session,request.META['HTTP_USER_AGENT'],request.COOKIES)
        password = request.POST.get("password")
        ip_address = modelCommon.getIpAddress(request)
        if not login_auth.login(mail_address,password,ip_address):
                err_message = login_auth.getMessage()
        if not request.session.get("user_id"):
                ctxt = {'err_message':err_message}
                
                return render(request, 'login.html', ctxt)
        else:
                response = redirect('/')
                return response