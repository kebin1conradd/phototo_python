
from ..dataBaseMapper.photos  import modelPhotos
from django.core.files.storage import default_storage
import os
import time
import mimetypes
class modelPhotoUpload():
	# upload image
	# @param files files
	# @param string title
	# @param int user_id
	# return false or int
	def upload(self,files,title,user_id):
		file_name = files["up_image"].name
		
		
		if file_name == '' or not files["up_image"]:
			return False	
		mimetypes.init()	
		ext = os.path.splitext(file_name)[1]
		mime = mimetypes.guess_type(file_name)
		if not ext.lower() in ['.jpg', '.png', '.jpeg','gif']:
			return False
		if not mime[0] in ['image/gif', 'image/jpeg', 'image/png']:
			return False		
		modelPhotos(
			title = title,
			extension_name = ext[1:],
			mime_type = mime[0],
			add_date = time.strftime('%Y-%m-%d %H:%M:%S'),
			user_id = user_id
			).save()
		row = modelPhotos.objects.latest()
		photo_id = row.photo_id
		
		default_storage.save(str(photo_id)+ext, files["up_image"])
		return photo_id	
