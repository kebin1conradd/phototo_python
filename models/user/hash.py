
import hashlib
import binascii
from django.utils.crypto import get_random_string
#セキュリティ確保のため一部文字列とロジックを変更しています


class modelUserHash():
	

	
	# change to hash from ip address
	#@param string ip_address
	#void
	def createTrip(self,ip_address):
		encrypt_str = 'encript_str'+ip_address
		salt = encrypt_str [-18:]
		temp_str = salt+ip_address
		trip = hashlib.md5(temp_str.encode('utf-8')).hexdigest()
		return trip[-10:]
		
	#create hash from register ip and ip hash and salt and raw password
	#@param string raw_password
	#@param string ip_trip
	#return string
	def createPasswordHash(self,raw_password,ip_trip):
		text = 'encript_str2'+ip_trip+raw_password
		return hashlib.sha256(text.encode('utf-8')).hexdigest()

	#create login token
	#@param int user_id
	#return string
	def createToken(self,user_id):
		string = str(user_id)+str(get_random_string(length=20))
		result = str(binascii.hexlify(str(string).encode('utf-8')))
		return result[2:32]

	#create activate code from register ip and raw password and ip trip
	#@param string mail_address
	#@param ip_trip
	#return string
	def createActivateCode(self,mail_address,ip_trip):
		text = 'encript_str3'+ip_trip+mail_address
		return hashlib.sha256(text.encode('utf-8')).hexdigest()


	