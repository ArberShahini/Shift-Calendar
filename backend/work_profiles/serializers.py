from rest_framework import serializers
from .models import WorkProfile
from companies.models import Company

class CreateWorkProfileSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = WorkProfile
        fields = [
            'company',
            'job_title',
            'hourly_pay',
            'start_time',
            'daily_hours',
            'workdays_per_week',
            'overtime_multiplier',
            'paid_leave_multiplier',
            'holiday_work_multiplier',
            'monthly_paid_leave',
            'is_company_admin'
        ]

class WorkProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProfile
        fields = [
            'id',
            'job_title',
            'start_time',
            'daily_hours',
            'is_company_admin'
        ]