from django.shortcuts import render
from ..models.user.create import modelUserCreate
from ..models.dataBaseMapper.usersActivation  import modelUsersActivation
from ..models.dataBaseMapper.users  import modelUsers
from django.template import RequestContext
from ..models.common import modelCommon
from cerberus import Validator

def index(request):
	error_occured = False
	ip_address = modelCommon.getIpAddress(request)
	password = request.POST.get("password")
	mail_address = request.POST.get("mail_address")
	user_name = request.POST.get("user_name")
	schema = {
		'mail_address': {
			'type': 'string',
			'required': True,
			'regex':'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
		},
		'password':{
			'type': 'string',
			'required': True,
			'minlength': 6,
		},
		'user_name': {
			'type': 'string',
			'required': True,
		},
	}
	validation = Validator(schema)
	validation_result = validation.validate({
		'password': password,
		"mail_address":mail_address,
		"user_name":user_name
		})
	if modelUsers.objects.filter(mail_address= mail_address).first() or modelUsersActivation.objects.filter(mail_address= mail_address).first():
		error_occured = True
		error_message = "Duplicated e-mail"

	elif not validation_result:
		error_occured = True
		error_message = validation.errors		
	else:
		create_origin = modelUserCreate()
		create_origin.createPreuser(password,user_name,mail_address,ip_address)

	if error_occured :
		ctxt = {"error_message":error_message }
		
		return render(request, 'userSignUp_error.html', ctxt)
	else:
		ctxt = {}
		
		return render(request, 'userSignUpRegister.html', ctxt)
