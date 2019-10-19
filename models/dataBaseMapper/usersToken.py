from django.db import models

class modelUsersToken(models.Model):
	user_id = models.IntegerField(primary_key=True)
	token = models.CharField(max_length=32)
	user_agent = models.CharField(max_length=255)
	class Meta:
		db_table = 'users_token' 