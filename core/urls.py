from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, summary_view
from rest_framework.authtoken.views import obtain_auth_token
from .views import export_employees_csv

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', summary_view, name='summary'),
    path('auth/token/', obtain_auth_token),
    path('export/csv/', export_employees_csv, name='export_csv'),  # CSV export route
]
