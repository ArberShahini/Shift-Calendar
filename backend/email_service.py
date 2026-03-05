from decouple import config
from django.core.mail import send_mail

class EmailService:
    @staticmethod
    def _send(to_email: str, subject: str, html_content: str):
        send_mail(
            subject=subject,
            message='',
            from_email=config('DEFAULT_FROM_EMAIL'),
            recipient_list=[to_email],
            html_message=html_content,
            fail_silently=False,
        )
        
    @staticmethod
    def send_activation_email(user, token: str):
        activation_url = f'{config('FRONTEND_URL')}/api/users/activate/{token}'
        html_content = f'''
            <h3>Activate your account</h3>
            <p>Hi {user.first_name},</p>
            <p>Click the link below to activate your account. This link expires in 24 hours.</p>
            <a href="{activation_url}">Activate Account</a>
        '''
        EmailService._send(user.email, 'Activate your account', html_content)

    @staticmethod
    def send_password_reset_email(user, token: str):
        reset_url = f'{config('FRONTEND_URL')}/api/users/password-reset/{token}'
        html_content = f'''
            <h3>Reset your password</h3>
            <p>Hi {user.first_name},</p>
            <p>Click the link below to reset your password. This link expires in 1 hour.</p>
            <a href="{reset_url}">Reset Password</a>
        '''
        EmailService._send(user.email, 'Reset your password', html_content)
