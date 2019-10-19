from django.db import models

class modelUsersActivation(models.Model):
	reserved_user_id = models.IntegerField(primary_key=True)
	password_hash = models.CharField(max_length=32)
	user_name = models.CharField(max_length=128)
	mail_address = models.CharField(max_length=254)
	activation_code = models.CharField(max_length=32)
	ip_address = models.CharField(max_length=15)
	is_activated = models.IntegerField()
	is_send = models.IntegerField()
	#本来DatetimeField型だが既存構造に対応していないため、Char型
	add_date = models.CharField(max_length=255)
	
	class Meta:
		db_table = 'users_activation' 
		get_latest_by = 'reserved_user_id'