from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.core import signing

class UserService:
    @staticmethod
    def register(data):
        user = User.objects.create_user(
            email=data['email'],
            password=data['password'],
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            timezone=data.get('timezone', 'UTC')
        )
        activation_token = UserService.generate_activation_token(user)
        return user, activation_token

    @staticmethod
    def generate_activation_token(user: User):
        return signing.dumps({'user_id': user.id}, salt='account-activation')

    @staticmethod
    def activate_account(token):
        try:
            data = signing.loads(token, salt='account-activation', max_age=86400)
        except signing.SignatureExpired:
            raise ValidationError({'error': 'Activation link has expired'})
        except signing.BadSignature:
            raise ValidationError({'error': 'Invalid activation link'})

        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            raise ValidationError({'error': 'User not found'})
        if user.is_active:
            raise ValidationError({'error': 'Account is already activated'})

        user.is_active = True
        user.save()
        return user

    @staticmethod
    def generate_pwd_reset_token(user: User):
        return signing.dumps({'user_id': user.id}, salt='password-reset')

    def reset_password(token, password):
        try:
            data = signing.loads(token, salt='password-reset', max_age=3600)
        except signing.SignatureExpired:
            raise ValidationError({'error': 'Password reset link has expired'})
        except signing.BadSignature:
            raise ValidationError({'error': 'Invalid password reset link'})

        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            raise ValidationError({'error': 'User not found'})

        user.set_password(password)
        user.save()
        return user

    @staticmethod
    def login(data, request):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise ValidationError({'error': 'Invalid credentials'})

        if not user.check_password(data['password']):
            raise ValidationError({'error': 'Invalid credentials'})

        if not user.is_active:
            raise ValidationError({'error': 'Account not activated'})

        if user.is_suspended:
            raise ValidationError({'error': 'Account is suspended'})

        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        }