from django.urls import path

from app.views import DepartmentsDetailView, DepartmentsListCreateView, EmployeesDetailView, EmployeesListCreateView, LocationsDetailView, LocationsListCreateView

urlpatterns = [
    path('employees/', EmployeesListCreateView.as_view(), name='employees-list-create'),
    path('employees/<int:pk>/', EmployeesDetailView.as_view(), name='employees-detail'),
    path('departments/', DepartmentsListCreateView.as_view(), name='departments-list-create'),
    path('departments/<int:pk>/', DepartmentsDetailView.as_view(), name='departments-detail'),
    path('locations/', LocationsListCreateView.as_view(), name='locations-list-create'),
    path('locations/<int:pk>/', LocationsDetailView.as_view(), name='locations-detail'),
]