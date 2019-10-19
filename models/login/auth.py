
from ..dataBaseMapper.usersActivation  import modelUsersActivation
from ..dataBaseMapper.users  import modelUsers
from ..dataBaseMapper.usersToken  import modelUsersToken
from ..user.hash  import modelUserHash
from ..common  import modelCommon
import time

class modelLoginAuth():
	message = ""
	message_status = False
	def __init__(self,session,user_agent,cookie):
		self.message = ""
		self.message_status = False
		self.session  = session
		self.user_agent = user_agent
		self.cookie = cookie
	# get normal logon
	# @patam string mail_address
	# @param string password
	# @param string ip_address
	# return boolean
	def login(self,mail_address,password,ip_address):
		
		user_encrypt = modelUserHash()
		if not mail_address  or not password:
			return False
		
		ip_trip = self.getTripFromMail(mail_address)
		password_hash = str(user_encrypt.createPasswordHash(password,ip_trip))
		rows = modelUsers.objects.only("user_id").filter(mail_address=mail_address,password_hash=password_hash).first()
		if not rows:
			self.setBadInputMessage()
			return False
		self.setUserInfoSession(rows.user_id)
		self.setLoginStatus(rows.user_id,ip_address,self.cookie)
		return True

	# first login
	# @param int user_id
	# @patam string ip_address
	def LoginFirstTime(self,user_id,ip_address):
		rows = modelUsers.objects.filter(user_id = user_id).first()
		self.setUserInfoSession(rows.user_id)
		self.setLoginStatus(rows.user_id,ip_address,self.cookie)
	
	
	# set information to session
	#@param object self 
	#@param int user_id
	#void
	def setUserInfoSession(self,user_id):
		rows = self.getLoginUserInfo(user_id)
		self.session['user_id'] = rows.user_id
	#get information of user
	#@param int user_id
	#return dict
	def getLoginUserInfo(self,user_id):
		rows = modelUsers.objects.filter(user_id=int(user_id)).first()
		return rows

	#get information of user from e-mail address
	#@param str mail_address
	#return dict
	def getLoginUserInfoFromMail(self,mail_address):
		rows = modelUsers.objects.filter(mail_address=mail_address).first()
		return rows

	#get ip_trip from users e-mail address
	#@param object self 
	#@param str mail_address
	#return string
	def getTripFromMail(self,mail_address):
		rows = self.getLoginUserInfoFromMail(mail_address)
		if rows :
			return rows.ip_trip
		else:
			return ""

	# if it's true, there is user on db
	# @param object self 
	# @param int user_id 
	#return boolean
	def isAvailableUser(self,user_id):		
		rows = self.getLoginUserInfo(user_id)
		if rows:
			return True
		else: 
			return False
	#when finished login set some related information on db
	#@param int user_id
	#@param string login_ip_address
	#@param request.session session
	#void
	def setLoginStatus(self,user_id,login_ip_address,cookie):
		user_encrypt = modelUserHash()
		token = user_encrypt.createToken(user_id)
		modelUsers.objects.filter(user_id=user_id).update(login_ip_address=login_ip_address)
		modelUsersToken.objects.update_or_create(user_id=user_id,  defaults={"user_agent":self.user_agent,"token":token})
		# logout
	# @param int user_id
	# void	
	def logout(self,user_id):
		modelUsersToken.objects.filter(user_id=user_id).delete()
		del self.session['user_id']
		
	


	def setBadInputMessage(self):
		self.message = "e-mailまたはpasswordが正しくありません"
	
	def getMessage(self):
		return self.message







