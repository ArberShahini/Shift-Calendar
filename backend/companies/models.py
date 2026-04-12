from django.db import models
import uuid, os

def logo_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    unique_name = uuid.uuid4().hex[:32]
    return f'logos/{unique_name}{ext}'

class Company(models.Model):
    name = models.CharField(max_length=256)
    country_code = models.CharField(max_length=2)
    logo = models.FileField(upload_to=logo_upload_path)

    class Meta:
        db_table = 'company'
        constraints = [
            models.UniqueConstraint(fields=['name', 'country_code'], name='company_name_country_unique')
        ]