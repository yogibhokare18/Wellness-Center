# 🌿 Wellness Center – Registration Management System

A web-based **Wellness Center Registration Management System** developed using **Python Flask, MySQL, HTML, CSS, and JavaScript**.

This project allows users to register by submitting their personal information through an online registration form. The registration details are securely stored in a MySQL database.

An administrator can log in through the Admin Login page and view all registered users through the Admin Dashboard.

---

## 📌 Project Overview

The **Wellness Center Registration Management System** is a Flask-based web application created to manage the registration process of a wellness center.

The system provides two main sections:

### 👤 User Section

Users can:

* Open the registration page
* Enter their personal details
* Enter their email and mobile number
* Select gender
* Enter date of birth
* Enter address
* Create a password
* Confirm their password
* Submit the registration form
* Receive a registration success message

### 👨‍💼 Admin Section

The administrator can:

* Access the Admin Login page
* Login using admin credentials
* View all registered users
* View registration details
* Logout from the admin panel

---

# ✨ Features

## 👤 User Registration

The registration form collects:

* Full Name
* Email Address
* Mobile Number
* Gender
* Date of Birth
* Address
* Password
* Confirm Password

---

## ✅ Backend Validation

The Flask backend validates the submitted information before storing it in the database.

### Name Validation

```python
if not name:
    return "Name is required!"
```

### Email Validation

```python
if not email:
    return "Email is required!"
```

### Mobile Number Validation

The system checks that the mobile number:

* Contains exactly 10 digits
* Contains numbers only

```python
if len(phone) != 10 or not phone.isdigit():
    return "Invalid mobile number!"
```

### Password Validation

The password must contain at least 8 characters.

```python
if len(password) < 8:
    return "Password must contain at least 8 characters!"
```

### Confirm Password Validation

The system checks whether the password and confirm password match.

```python
if password != confirm_password:
    return "Password and Confirm Password do not match!"
```

---

# 🔐 Password Security

User passwords are **not stored as plain text**.

The project uses Werkzeug's password hashing functionality:

```python
from werkzeug.security import generate_password_hash
```

The password is converted into a secure hash before being inserted into the database.

```python
hashed_password = generate_password_hash(password)
```

The database therefore stores the hashed password instead of the original password.

---

# 🗄️ Database

The project uses **MySQL** as its database.

### Database Name

```text
wellness_db
```

### Main Table

```text
registrations
```

---

# 📋 Registrations Table

The `registrations` table contains the following fields:

| Column     | Data Type    | Description                |
| ---------- | ------------ | -------------------------- |
| id         | INT          | Unique registration ID     |
| name       | VARCHAR(100) | User's full name           |
| email      | VARCHAR(100) | User's email address       |
| phone      | VARCHAR(10)  | User's mobile number       |
| gender     | VARCHAR(20)  | User's gender              |
| dob        | DATE         | User's date of birth       |
| address    | VARCHAR(255) | User's address             |
| password   | VARCHAR(255) | Hashed password            |
| created_at | TIMESTAMP    | Registration date and time |

The `email` column is configured as **UNIQUE**, which prevents duplicate registrations using the same email address.

---

# 🗃️ Database SQL File

The project contains:

```text
wellness_db.sql
```

This file can be used to create the database and registration table.

Example:

```sql
CREATE DATABASE IF NOT EXISTS wellness_db;

USE wellness_db;

CREATE TABLE IF NOT EXISTS registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(10) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    dob DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# 🔄 Application Flow

```text
                    ┌──────────────────┐
                    │    Home Page     │
                    │  Registration    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Registration Form│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Backend          │
                    │ Validation       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Password Hashing │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ MySQL Database   │
                    │ registrations    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Success Page     │
                    └──────────────────┘
```

---

# 👨‍💼 Admin Flow

```text
              ┌────────────────────┐
              │   Admin Login      │
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │ Username & Password│
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │ Authentication     │
              └─────────┬──────────┘
                        │
                  Valid Credentials
                        │
                        ▼
              ┌────────────────────┐
              │ Admin Dashboard    │
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │ View Registrations │
              └────────────────────┘
```

---

# 🔐 Admin Authentication

The project uses Flask sessions to maintain the admin login state.

The session is created after successful login:

```python
session["admin_logged_in"] = True
```

The Admin Dashboard checks whether the administrator is logged in.

```python
if not session.get("admin_logged_in"):
    return redirect(url_for("admin_login"))
```

If the admin is not logged in, the user is redirected to the Admin Login page.

---

# 👨‍💼 Admin Login

The current project uses temporary admin credentials:

```text
Username: admin
Password: admin123
```

> ⚠️ These credentials are currently hard-coded in `app.py` for development purposes. For a production application, admin authentication should be implemented securely using a database, password hashing, environment variables, and proper authentication mechanisms.

---

# 📊 Admin Dashboard

After successful admin login, the administrator is redirected to:

```text
/admin/
```

The Admin Dashboard displays registered users from the `registrations` table.

The following information is displayed:

* Registration ID
* Name
* Email
* Phone
* Gender
* Date of Birth
* Address
* Registration Date

The registrations are retrieved using:

```sql
SELECT
    id,
    name,
    email,
    phone,
    gender,
    dob,
    address,
    created_at
FROM registrations
ORDER BY id ASC;
```

---

# 🚪 Admin Logout

The administrator can logout using:

```text
/admin/logout
```

The session is removed using:

```python
session.pop("admin_logged_in", None)
```

After logout, the administrator is redirected to the Admin Login page.

---

# 🌐 Application Routes

The current Flask application contains the following routes:

| Method | Route           | Purpose                   |
| ------ | --------------- | ------------------------- |
| GET    | `/`             | Display registration page |
| POST   | `/register`     | Process user registration |
| GET    | `/admin/login`  | Display admin login       |
| POST   | `/admin/login`  | Authenticate admin        |
| GET    | `/admin/`       | Display admin dashboard   |
| GET    | `/admin/logout` | Logout admin              |

---

# 🏗️ Project Structure

```text
Wellness-Center/
│
├── app.py
├── config.py
├── wellness_db.sql
├── requirements.txt
├── README.md
│
├── templates/
│   ├── register.html
│   ├── success.html
│   ├── admin_login.html
│   └── admin.html
│
└── static/
    │
    ├── css/
    │   ├── style.css
    │   └── admin.css
    │
    └── js/
        └── script.js
```

> The exact filenames should match the files present in your project folder.

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask

## Database

* MySQL

## Python Libraries

* Flask
* mysql-connector-python
* Werkzeug

## Development Tools

* Visual Studio Code
* MySQL Workbench
* Git
* GitHub

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Wellness-Center
```

---

## 2. Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Required Packages

Install Flask:

```bash
pip install flask
```

Install MySQL Connector:

```bash
pip install mysql-connector-python
```

Install Werkzeug:

```bash
pip install werkzeug
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

# 🗄️ 4. Configure MySQL

Start your MySQL Server.

Create the database:

```sql
CREATE DATABASE wellness_db;
```

Then select the database:

```sql
USE wellness_db;
```

Create the registration table:

```sql
CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(10) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    dob DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Alternatively, import:

```text
wellness_db.sql
```

into MySQL.

---

# ⚙️ 5. Configure Database Connection

The project uses:

```python
from config import DB_CONFIG
```

The database configuration is stored in:

```text
config.py
```

Example:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "wellness_db"
}
```

Replace:

```text
YOUR_MYSQL_PASSWORD
```

with your local MySQL password.

> ⚠️ Never upload your actual database password to GitHub.

---

# ▶️ 6. Run the Application

Activate your virtual environment:

```bash
venv\Scripts\activate
```

Run the Flask application:

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser.

---

# 📝 User Registration

Open:

```text
http://127.0.0.1:5000/
```

Enter the required details and submit the registration form.

After successful registration, the application displays the registration success page.

---

# 🔑 Admin Login

Open:

```text
http://127.0.0.1:5000/admin/login
```

Use the development credentials:

```text
Username: admin
Password: admin123
```

After successful authentication, the application redirects to:

```text
http://127.0.0.1:5000/admin/
```

---

# 📊 Admin Dashboard

The dashboard displays all registrations stored in the MySQL database.

Example information:

```text
ID
Name
Email
Phone
Gender
Date of Birth
Address
Created At
```

---

# 🧪 Error Handling

The project handles duplicate email registration using MySQL's `UNIQUE` constraint.

If an email is already registered, the application returns:

```text
Email already registered!
```

The project also validates:

* Empty name
* Empty email
* Invalid mobile number
* Short password
* Password mismatch

---

# 🔒 Security Considerations

The project implements basic security features:

* Password hashing using Werkzeug
* Backend validation
* Unique email constraint
* Flask session-based admin authentication
* Protected Admin Dashboard
* Database constraints

For production deployment, the following should be improved:

* Store `SECRET_KEY` in environment variables
* Store admin credentials securely
* Use hashed admin passwords
* Add CSRF protection
* Use HTTPS
* Validate and sanitize all inputs
* Use environment variables for database credentials
* Disable Flask debug mode
* Use a production WSGI server

---

# 📸 Screenshots

Add screenshots of your actual website here.

Recommended screenshots:

```text
1. Registration Page
2. Registration Success Page
3. Admin Login Page
4. Admin Dashboard
```

Example:

```markdown
## 📸 Screenshots

### Registration Page

![Registration Page](screenshots/register.png)

### Registration Success Page

![Success Page](screenshots/success.png)

### Admin Login

![Admin Login](screenshots/admin-login.png)

### Admin Dashboard

![Admin Dashboard](screenshots/admin-dashboard.png)
```

---

# 🚀 Future Enhancements

The following features can be added in future versions:

* ✏️ Edit Registration
* 🗑️ Delete Registration
* 🔍 Search Registration
* 🔎 Filter Users
* 📄 Export Registration Data
* 📊 Dashboard Statistics
* 📥 Export to Excel
* 📄 Generate PDF Reports
* 📧 Email Confirmation
* 🔐 Secure Admin Authentication
* 👥 Multiple Admin Accounts
* 🔑 Forgot Password
* 📱 Improved Mobile Responsiveness
* ☁️ Deploy Application Online

---

# 🎯 Project Objectives

The main objectives of this project are:

1. To create an online registration system for a Wellness Center.
2. To store registration information in a MySQL database.
3. To reduce manual registration work.
4. To provide backend validation for user data.
5. To provide an admin dashboard for viewing registrations.
6. To implement basic authentication and session management.
7. To create a simple and user-friendly web interface.

---

# 💡 Learning Outcomes

Through this project, the following concepts were implemented:

* Flask Web Development
* Flask Routing
* HTML Forms
* CSS Styling
* JavaScript Validation
* Backend Validation
* MySQL Database Connectivity
* SQL Queries
* CRUD-related database concepts
* Password Hashing
* Flask Sessions
* Admin Authentication
* Jinja2 Templates
* Git & GitHub Project Management

---

# 👨‍💻 Developer

## Yoginand Digambar Bhokare

**BCA Graduate | Full Stack Developer**

### Technical Skills

```text
Python
Flask
MySQL
HTML
CSS
JavaScript
Git
GitHub
```

---

# 📄 License

This project is developed for **educational, learning, and portfolio purposes**.

---

# ⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.

**Thank you for visiting the Wellness Center Registration Management System! 🌿**
