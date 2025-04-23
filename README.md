Employee Management System
This project is a basic Employee Management System built with Django and Django REST Framework (DRF). It allows for the generation of synthetic employee data, storing the data in a PostgreSQL database, and provides a REST API for interacting with the data. Additionally, it supports exporting employee data to a CSV file and integrates Swagger UI for API documentation.

Features
Generate synthetic employee records using the Faker library.

Store employee data in a PostgreSQL database.

Provide REST API endpoints for employees and departments.

Generate analytical summaries of employee data.

Export employee data to a CSV file.

Interactive API documentation using Swagger UI (drf-yasg).

Authentication via Token-based authentication (using DRF's obtain_auth_token).

Technologies Used
Backend Framework: Django

REST Framework: Django REST Framework (DRF)

Database: PostgreSQL

Data Generation: Faker

CSV Export: Python's csv module

API Documentation: drf-yasg for Swagger UI

Authentication: Token-based authentication

Requirements
Python 3.8 or above

PostgreSQL

pip (for Python dependencies)

Setup Instructions
1. Clone the Repository
Clone the project to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/employee-management-system.git
cd employee-management-system
2. Set Up Virtual Environment
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
Install the required dependencies using pip:

bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root directory to store environment-specific configurations, such as your PostgreSQL database credentials.

Example .env file:

ini
Copy
Edit
DEBUG=True
DATABASE_URL=postgres://username:password@localhost:5432/employee_db
SECRET_KEY=your-secret-key
5. Set Up PostgreSQL Database
Make sure you have PostgreSQL installed and a database set up. Run the following commands to create a new database:

bash
Copy
Edit
# Access PostgreSQL prompt
psql -U postgres
# Create a new database
CREATE DATABASE employee_db;
Update the DATABASE_URL in your .env file to match your PostgreSQL setup (e.g., postgres://postgres:password@localhost:5432/employee_db).

6. Apply Migrations
Run the Django migrations to set up the database schema:

bash
Copy
Edit
python manage.py migrate
7. Create Superuser (Optional)
If you want to access the Django Admin interface, create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to create a user.

8. Generate Synthetic Data (Optional)
You can generate synthetic employee data by running the following command:

bash
Copy
Edit
python manage.py shell
>>> from core.seed import generate_fake_data
>>> generate_fake_data()
9. Run the Server
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
You can now access the application at http://127.0.0.1:8000/.

API Endpoints
1. /api/employees/
Method: GET, POST

Description: List all employees or create a new employee.

Query Parameters:

department: Filter employees by department.

search: Search employees by name, job title, etc.

2. /api/departments/
Method: GET

Description: List all departments.

3. /api/summary/
Method: GET

Description: Get an analytical summary of the employee data, including average salary, employee count per department, etc.

4. /api/export/csv/
Method: GET

Description: Export all employee data to a CSV file.

5. /api/auth/token/
Method: POST

Description: Obtain a token for authentication.

Request Body:

json
Copy
Edit
{
  "username": "your-username",
  "password": "your-password"
}
Swagger UI
You can view and interact with the API using Swagger UI:

Go to http://127.0.0.1:8000/swagger/

Additional Features (Optional)
CSV Export

To export employee data to CSV, visit http://127.0.0.1:8000/api/export/csv/.


Troubleshooting
404 Error on /api/export/csv/: Ensure that the URL pattern in core/urls.py includes the correct path for the export route: path('export/csv/', export_employees_csv, name='export_csv').

Database Errors: Make sure your PostgreSQL database is running and configured correctly in the .env file.

License
MIT License
