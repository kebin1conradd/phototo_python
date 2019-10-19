from django.db import models

class modelPhotos(models.Model):
	photo_id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=255)
	extension_name = models.CharField(max_length=10)
	mime_type = models.CharField(max_length=30)
	#本来DatetimeField型だが既存構造に対応していないため、Char型
	add_date = models.CharField(max_length=255)
	edit_date = models.CharField(max_length=255)
	user_id = models.IntegerField()
	class Meta:
		db_table = 'photos' 
		get_latest_by = 'photo_id'