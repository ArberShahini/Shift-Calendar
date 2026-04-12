from django.db import models
from companies.models import Company

class WorkProfile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    hourly_pay = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.TimeField()
    daily_hours = models.DecimalField(max_digits=4, decimal_places=2)
    workdays_per_week = models.IntegerField()
    overtime_multiplier = models.DecimalField(max_digits=3, decimal_places=2)
    paid_leave_multiplier = models.DecimalField(max_digits=3, decimal_places=2)
    holiday_work_multiplier = models.DecimalField(max_digits=3, decimal_places=2)
    monthly_paid_leave = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_company_admin = models.BooleanField()

    class Meta:
        db_table = 'work_profile'