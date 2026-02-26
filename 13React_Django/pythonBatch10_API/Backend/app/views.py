from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from app.models import Departments, Employees, Locations
from app.serializers import DepartmentsSerializer, EmployeesSerializer, LocationsSerializer
  

class EmployeesListCreateView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class EmployeesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    
class DepartmentsListCreateView(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer

class DepartmentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    
class LocationsListCreateView(generics.ListCreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

class LocationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer