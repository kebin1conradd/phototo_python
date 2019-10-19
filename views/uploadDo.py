from django.shortcuts import render
from ..models.photo.upload import modelPhotoUpload

from django.template import RequestContext
from ..models.common import modelCommon
from cerberus import Validator

def index(request):
	error_occured = False
	user_id = request.session.get("user_id")
	title = request.POST.get("title")	
	schema = {
		'title':{
			'type': 'string',
			'required': True,
		},
	}
	validation = Validator(schema)
	validation_result = validation.validate({
		'title': title,
		})
	if not user_id:
		error_occured = True
		error_message = 'ログインいていません。'
	elif not validation_result:
		error_occured = True
		error_message = validation.errors		
	else:
		photo_upload = modelPhotoUpload()
		photo_id = photo_upload.upload(request.FILES,title,user_id)
		if not photo_id:
			error_occured = True
			error_message = 'upload中にエラーが発生しました。ファイル形式を確認してください。'
	if error_occured :
		ctxt = {"error_message":error_message }
		
		return render(request, 'uploadErr.html', ctxt)
	else:
		ctxt = {"photo_id":photo_id}
		
		return render(request, 'uploadSuccess.html', ctxt)
