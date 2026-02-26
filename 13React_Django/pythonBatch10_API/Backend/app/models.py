from django.db import models

# Create your models here.

class Employees(models.Model):
    employee_id = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    department_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Departments(models.Model):
    department_id = models.CharField(max_length=100)
    departmentName = models.CharField(max_length=100)
    location_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Locations(models.Model):
    location_id = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
