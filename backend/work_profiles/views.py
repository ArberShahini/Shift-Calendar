from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import *
from .services import WorkProfileService
from .models import WorkProfile

class CreateWorkProfileView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateWorkProfileSerializer(data=request.data)
        if serializer.is_valid():
            workProfile = WorkProfileService.create(serializer.validated_data)
            return Response({'message': 'Work profile created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getWorkProfileByIdView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, company_id):
        workProfiles_data = WorkProfileService.getByCompanyId(company_id)
        serializer = WorkProfileSerializer(workProfiles_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)