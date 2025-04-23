from faker import Faker
from core.models import Employee, Department, Attendance, PerformanceReview, SalaryRecord
import random
from datetime import timedelta
from django.utils import timezone

fake = Faker()

def generate_fake_data():
    departments = [Department.objects.create(name=fake.company(), location=fake.city()) for _ in range(3)]

    for _ in range(5):
        dept = random.choice(departments)
        emp = Employee.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
            position=fake.job(),
            department=dept,
            hired_date=fake.date_between(start_date='-2y', end_date='-1d'),
            salary=round(random.uniform(40000, 100000), 2),
            active=random.choice([True, False])
        )

        # Attendance
        for i in range(5):
            Attendance.objects.create(
                employee=emp,
                date=timezone.now().date() - timedelta(days=i),
                status=random.choice(['Present', 'Absent'])
            )

        # Performance Review
        PerformanceReview.objects.create(
            employee=emp,
            review_date=fake.date_between(start_date='-1y', end_date='today'),
            score=random.randint(1, 10),
            feedback=fake.sentence()
        )

        # Salary history
        for _ in range(2):
            SalaryRecord.objects.create(
                employee=emp,
                effective_date=fake.date_between(start_date='-2y', end_date='today'),
                amount=round(random.uniform(40000, 120000), 2)
            )

    print("🌱 Seed data created.")
