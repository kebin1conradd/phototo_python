from django.core.mail import send_mail

class modelUserMail():
	
	# send mail for user authoricate
	# @param string activation_code
	# @param string mail_address
	# @param int reserved_user_id
	def sendActivateMail(self,activation_code,mail_address,reserved_user_id):
		body = self._getActivateMessage(activation_code,reserved_user_id)
		subject = self._getActivateSubject()

		send_mail(subject, body, 'noreply@phototo.nl', [mail_address])
		

	# sending message
	# @param string activation_code
	# @param int rserved_user_id
	# @return string
	def _getActivateMessage(self,activation_code,rserved_user_id):
		return 'このたびは、フォトットへの登録ありがとうございます 確認のため、下記URLへアクセスしアカウントの登録を完了させてください。http://ec2-34-210-85-98.us-west-2.compute.amazonaws.com/userMailConfirmation/?activation_code='+activation_code+'&reserved_user_id='+str(rserved_user_id)
	# sending subject
	# @return string
	def _getActivateSubject(self):
		return 'フォトット 会員登録メール'


	