# Underdevelopment!
# Inventory Management System

## Project Description
This is a Django-based Inventory Management System designed to manage various aspects of inventory, user authentication, and dashboards for different user roles. The project includes multiple Django apps such as Admin, FarmersDashboard, and LoginLogout, providing a modular structure for managing different functionalities.

The system features:
- User authentication and registration
- Admin dashboard and management
- Farmer's dashboard for inventory and related operations
- Static and dynamic pages including Landing Page, About Us, and Contact Us

**Note:** This project is currently under development.

## Technologies Used
- Python 3.x
- Django 5.2.3
- MySQL Database
- Tailwind CSS for styling
- Other dependencies as listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd inventoryManagementSystem/Manager
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the `Manager` directory.
   - Add the following environment variables:
     ```
     SECRET_KEY=your_django_secret_key
     ```

5. Configure MySQL database:
   - Ensure MySQL server is running.
   - Create a database named `IMS`.
   - Update database credentials in `Manager/settings.py` if necessary.

6. Apply migrations:
   ```bash
   python manage.py migrate
   ```

7. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Development Server

Start the Django development server with:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

## Project Structure Overview

- `Admin/` - Django app for admin functionalities.
- `FarmersDashboard/` - Django app for farmer's dashboard and inventory management.
- `LoginLogout/` - Django app handling user authentication and registration.
- `Manager/` - Project configuration, settings, URLs, and main views.
- `templates/` - Global templates including LandingPage, AboutUs, ContactUs.
- `static/` - Static files such as CSS and JavaScript.
- `requirements.txt` - Python dependencies.

## Main URLs

- `/` - Landing Page
- `/about/` - About Us page
- `/contact/` - Contact Us page
- `/dashboard/` - Farmer's dashboard (requires login)
- `/custom_admin/` - Admin dashboard and management
- `/login/` - User login and registration
- `/admin/` - Django admin interface

## Notes

- Debug mode is enabled by default. Disable it in production by setting `DEBUG = False` in `Manager/settings.py`.
- Static files are served from `/static/`.
- Login URL is set to `/admin/login/` by default.
- Ensure to keep the `SECRET_KEY` secure and do not expose it publicly.

## License

This project does not specify a license. Please add a license file if you intend to distribute it.

