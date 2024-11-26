**RBAC (Role-Based Access Control) System**
**Project Overview**
This project implements a Role-Based Access Control (RBAC) system using Django. It allows users to register, login, and access different sections of the application based on their roles (Admin, Moderator, User). The project demonstrates how to manage user roles and their corresponding permissions within a web application.

**Admin** users can access all the features and manage users and data.
**Moderators** can moderate content but with limited permissions.
**Users** can only view content and have read-only access.
This project demonstrates a typical user authentication and authorization system used in web applications, ensuring proper access control.

**Features**
**User Registration:** Users can sign up by providing their details.
**User Login:** Registered users can log in to the application.
**Role-Based Access Control:** Based on the user role (Admin, Moderator, or User), different access levels are granted.
**Admin:** Full access to all views and management features.
**Moderator**: Access to moderate content, but restricted from administrative features.
**User:** View-only access with basic permissions.
**Logout:** Users can log out of the system.
**Profile Pages:** Each role has a dedicated profile page with specific functionalities.

**Setup Instructions**
Follow these steps to run the project locally on your machine:

**1. Clone the Repository**
git clone https://github.com/kumarnamburi02/rbac.git

**2. Install Python and Django**
Make sure you have Python installed. You can check it by running:
python --version

**3. Create a Virtual Environment**
cd rbac
python -m venv venv

**4. Activate the Virtual Environment**
**For Windows:**
venv\Scripts\activate

**For Mac/Linux:**
source venv/bin/activate

**5. Install Dependencies**
Once the virtual environment is activated, install the required dependencies from the requirements.txt file:
pip install -r requirements.txt

**6. Apply Migrations**
Before running the project, make sure to apply the database migrations to create the necessary tables:
python manage.py migrate

**7. Run the Development Server**
Start the Django development server:
python manage.py runserver
This will start the server, and you can access the project in your browser at http://127.0.0.1:8000/.

**Dependencies**
This project requires the following dependencies:

**Python 3.x**
**Django:** A high-level Python web framework.
**djangorestframework:** A toolkit for building Web APIs in Django.
**djangorestframework-simplejwt:** A library to handle JWT authentication in Django.
**django-cors-headers:** A library to manage Cross-Origin Resource Sharing (CORS) headers.
**Python-dotenv:** For managing environment variables.

**You can install all the required dependencies with:**
pip install -r requirements.txt

**Running the Tests**
To run the tests for this project (if you have written any tests), use the following command:
python manage.py test

**File Structure**
The file structure for this project is as follows:
rbac/
│
├── accounts/                    # Account and user-related views, models, and serializers
│   ├── migrations/
│   ├── models.py                # CustomUser and Profile models
│   ├── serializers.py           # User and Login serializers
│   ├── views.py                 # Views for registration, login, etc.
│   ├── urls.py                  # URL routing for accounts app
│   ├── permissions.py           # Custom permissions for Admin, Moderator, User
│   └── ...
│
├── rbac_project/                # Main project folder
│   ├── settings.py              # Django settings file
│   ├── urls.py                  # Main URL routing for the project
│   ├── wsgi.py                  # WSGI entry point for running the application
│   └── ...
│
├── templates/                   # Template files (HTML)
│   ├── home.html                # Home page template
│   └── ...
│
├── static/                      # Static files (CSS, JavaScript)
├── requirements.txt             # List of dependencies
├── manage.py                    # Django management script
└── README.md                    # Project documentation (this file)

**Acknowledgments**
Thanks to the Django team for the great framework.
Thanks to the community for helping with documentation and troubleshooting.
