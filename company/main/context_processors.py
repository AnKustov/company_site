from office.models import *

def company_data(request):
    company = Company.objects.first()
    return {'company': company}
