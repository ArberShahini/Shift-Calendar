from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import *
from .services import UserService
from .models import User
import email_service

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user, token = UserService.register(serializer.validated_data)
            email_service.EmailService.send_activation_email(user, token)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                tokens = UserService.login(serializer.validated_data, request)
                return Response(tokens, status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response(e.detail, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountActivationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        UserService.activate_account(token)
        return Response({'message': 'Account has been activated successfully'})

class PwdResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PwdResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                token = UserService.generate_pwd_reset_token(user)
                email_service.EmailService.send_password_reset_email(user, token)
            except User.DoesNotExist:
                pass
            return Response({'message': 'If this email exists you will receive a password reset link'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PwdResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, token):
        serializer = PwdResetSerializer(data=request.data)
        if serializer.is_valid():
            UserService.reset_password(token, serializer.validated_data['password'])
            return Response({'message': 'Password has been changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)