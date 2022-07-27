from django.db import models
from tastypie.resources import ModelResource
from home.models import Employees


# Create your models here.
class EmployeesResource(ModelResource):
    class Meta:
        queryset = Employees.objects.all()
        resource_name = 'api'
