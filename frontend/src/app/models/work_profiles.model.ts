export interface WorkProfile {
    id: number;
    company: number;
    job_title: string;
    hourly_pay: number;
    start_time: string;
    daily_hours: number;
    workdays_per_week: number;
    overtime_multiplier: number;
    paid_leave_multiplier: number;
    holiday_work_multiplier: number;
    monthly_paid_leave: number;
    is_company_admin: boolean;
}