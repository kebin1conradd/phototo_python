
from ..dataBaseMapper.usersActivation  import modelUsersActivation
from ..dataBaseMapper.users  import modelUsers
from .mail import modelUserMail
from .hash  import modelUserHash
import time
class modelUserCreate():
	

	
	# create user data that is before mail authorication
	# @param string password 
	# @param string user_name
	# @param string mail_address 
	# @param string ip_address 
	# void
	def createPreuser(self,password,user_name,mail_address,ip_address):
		user_encrypt = modelUserHash()
		user_mail = modelUserMail()
		ip_trip = user_encrypt.createTrip(ip_address)
		activation_code = user_encrypt.createActivateCode(mail_address,ip_trip)
		password_hash = user_encrypt.createPasswordHash(password,ip_trip)
		modelUsersActivation(
			password_hash = password_hash,
			user_name = user_name,
			mail_address = mail_address,
			ip_address = ip_address,
			activation_code = activation_code,
			is_activated = 0,
			is_send = 1,
			add_date = time.strftime('%Y-%m-%d %H:%M:%S')
		).save()
		row = modelUsersActivation.objects.latest()
		reserved_user_id = row.reserved_user_id

		user_mail.sendActivateMail(activation_code,mail_address,reserved_user_id)

	# create user from activation user table on details user table
	# @param int reserved_user_id
	# return mixed int or false
	def createUserFromPreId(self,reserved_user_id):
		rows = modelUsersActivation.objects.filter(reserved_user_id = reserved_user_id).first()
		if rows:
			user_id = self.createUser(rows.password_hash, rows.user_name, rows.mail_address, rows.ip_address)
			rows.is_activated = 1
			rows.save()
			return user_id
		else:
			return False	
	# get correspond ip
	# @param string activation_code
	# @param int reserved_user_id
	# return boolean
	def isActivate(self,activation_code,reserved_user_id):
		rows = modelUsersActivation.objects.filter(reserved_user_id = reserved_user_id,activation_code = activation_code).first()
		if rows:
			return True
		else:
			return False
	# create user information on table
	# @param string password
	# @param string user_name
	# @param string mail_address
	# @param string ip_address
	# return int insert id
	def  createUser(self,password_hash,user_name,mail_address,ip_address):
		user_encrypt = modelUserHash()
		ip_trip = user_encrypt.createTrip(ip_address)
		modelUsers(
			password_hash = password_hash,
			user_name = user_name,
			mail_address = mail_address,
			register_ip_address = ip_address,
			add_date = time.strftime('%Y-%m-%d %H:%M:%S'),
			ip_trip = ip_trip
		).save()
		row = modelUsers.objects.latest()
		return row.user_id