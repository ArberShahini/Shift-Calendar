from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import *
from .services import CompanyService
from .models import Company

class CompanyRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            company = CompanyService.create(serializer.validated_data)
            return Response({'message': 'Company created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyGetAllView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        company_data = CompanyService.get_all()
        serializer = CompanySerializer(company_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
