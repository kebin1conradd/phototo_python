from django.shortcuts import render
from ..models.user.create import modelUserCreate
from ..models.login.auth import modelLoginAuth
from django.template import RequestContext
from ..models.common import modelCommon


def index(request):
	error_occured = False
	create_origin = modelUserCreate()
	ip_address = modelCommon.getIpAddress(request)
	activation_code = request.GET.get("activation_code")
	reserved_user_id= request.GET.get("reserved_user_id")
	login_auth = modelLoginAuth(request.session,request.META['HTTP_USER_AGENT'],request.COOKIES)
	if create_origin.isActivate(activation_code,reserved_user_id):
		user_id = create_origin.createUserFromPreId(reserved_user_id)
		if user_id:
			login_auth.LoginFirstTime(user_id,ip_address)		
	else:
		error_occured = True

	if error_occured :
		ctxt = {"is_activate_invalid":True }
		
		return render(request, 'userMailauthErr.html', ctxt)
	else:
		ctxt = {}
		
		return render(request, 'userMailauth.html', ctxt)