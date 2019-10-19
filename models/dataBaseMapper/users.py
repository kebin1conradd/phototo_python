from django.db import models

class modelUsers(models.Model):

	user_id = models.IntegerField(primary_key=True)
	password_hash = models.CharField(max_length=32)
	user_name = models.CharField(max_length=128)
	description = models.CharField(max_length=255)
	#本来DatetimeField型だが既存構造に対応していないため、Char型
	add_date = models.CharField(max_length=255)
	mail_address = models.CharField(max_length=254)
	register_ip_address = models.CharField(max_length=15)
	login_ip_address = models.CharField(max_length=15)
	ip_trip= models.CharField(max_length=32)
	class Meta:
		db_table = 'users' 
		get_latest_by = 'user_id'