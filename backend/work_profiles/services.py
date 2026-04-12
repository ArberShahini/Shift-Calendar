from .models import WorkProfile

class WorkProfileService:
    @staticmethod
    def create(data):
        workProfile = WorkProfile.objects.create(
            company = data['company'],
            job_title = data['job_title'],
            hourly_pay = data['hourly_pay'],
            start_time = data['start_time'],
            daily_hours = data['daily_hours'],
            workdays_per_week = data['workdays_per_week'],
            overtime_multiplier = data['overtime_multiplier'],
            paid_leave_multiplier = data['paid_leave_multiplier'],
            holiday_work_multiplier = data['holiday_work_multiplier'],
            monthly_paid_leave = data['monthly_paid_leave'],
            is_company_admin = data['is_company_admin']
        )
        return workProfile

    @staticmethod
    def getByCompanyId(company_id):
        workProfiles = WorkProfile.objects.filter(company_id=company_id, is_company_admin=False)
        return workProfiles