from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_confirmation(data):
        confirmation_email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['email_to']])
        confirmation_email.send()
