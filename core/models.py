from django.db import models

# Create your models here.
# core/models.py (example snippet)
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    hired_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()
    feedback = models.TextField()

class SalaryRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)