# core/views.py
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
import csv
from django.http import HttpResponse
from .models import Employee

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['department', 'active']
    search_fields = ['name', 'email', 'position']
    ordering_fields = ['salary', 'hired_date']

@api_view(['GET'])
def summary_view(request):
    avg_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))['avg_salary']
    dept_counts = Employee.objects.values('department__name').annotate(count=Count('id'))

    return Response({
        'average_salary': avg_salary,
        'employees_per_department': dept_counts
    })
def export_employees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Position', 'Department', 'Hired Date', 'Salary', 'Active'])

    for emp in Employee.objects.select_related('department').all():
        writer.writerow([
            emp.name,
            emp.email,
            emp.position,
            emp.department.name,
            emp.hired_date,
            emp.salary,
            emp.active,
        ])

    return response