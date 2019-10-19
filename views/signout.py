
from django.template import RequestContext
from django.shortcuts import render
from ..models.login.auth import modelLoginAuth
from django.template import RequestContext

from django.shortcuts import redirect
def index(request):
        

        if not request.session.get("user_id"):
                ctxt = {}
                
                return render(request, 'Signout_error.html', ctxt)
        else:
                login_auth = modelLoginAuth(request.session,request.META['HTTP_USER_AGENT'],request.COOKIES)
                login_auth.logout(request.session.get("user_id"))
                response = redirect('/')
                return response