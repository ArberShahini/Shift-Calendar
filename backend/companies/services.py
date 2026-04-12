from .models import Company

class CompanyService:
    @staticmethod
    def create(data):
        company = Company.objects.create(
            name = data['name'],
            country_code = data['country_code'],
            logo = data['logo'] 
        )
        return company

    @staticmethod
    def get_all():
        companies = Company.objects.all()
        return companies