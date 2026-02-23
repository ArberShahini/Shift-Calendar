from .models import User

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
        return user