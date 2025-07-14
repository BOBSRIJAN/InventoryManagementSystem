# Underdevelopment!

# Inventory Management System

## Project Overview
This is an Inventory Management System built using Django. The system manages different user roles including Admin, Farmers, Shopkeepers, and general Users. It provides functionalities such as inventory management, user authentication, and reporting.

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
