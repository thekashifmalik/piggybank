from django.conf import settings
from django.core import mail

def send_mail(subject, message, recipient_list, fail_silently=False):
	"""Send Mail

	Wrapper around 'django.core.mail.send_mail' to send mail using the admin
	user defined in the settings.

	"""
	return mail.send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=fail_silently)
