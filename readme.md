# Inventory Management System

## Project Overview
This Inventory Management System is a comprehensive web application built using Django, designed to efficiently manage inventory operations across multiple user roles. The system supports Admins, Farmers, Shopkeepers, and general Users, each with tailored functionalities to streamline inventory management, user authentication, and reporting.

## Key Features
- Role-based access control for Admin, Farmers, Shopkeepers, and Users
- Inventory management tailored for Farmers and Shopkeepers
- User authentication and authorization with secure login and registration
- Administrative dashboard for managing users and overseeing system operations
- Reporting and data visualization capabilities (if applicable)
- Responsive and user-friendly interface

## Technologies Used
- Python 3.x
- Django Web Framework
- HTML, CSS, JavaScript for frontend templates and static assets
- SQLite/MySQL/PostgreSQL (depending on configuration) for database
- Other Python dependencies as listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd Manager
   ```
3. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Apply migrations:
   ```
   python manage.py migrate
   ```
2. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```
3. Run the development server:
   ```
   python manage.py runserver
   ```
4. Access the application in your browser at:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure and Main Apps

- **Admin**: Handles administrative functionalities and dashboard.
- **Auth**: Manages user authentication including login and registration.
- **Farmers**: Manages farmer-specific inventory and marketplace features.
- **Shopkeeper**: Manages shopkeeper-related inventory and operations.
- **User**: General user management and profiles.

## Dependencies

- Django (version as per requirements.txt)
- Other dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License. See the LICENSE file for details.
