from flask import Flask, render_template, request, session, redirect, url_for

import mysql.connector

from werkzeug.security import generate_password_hash

from config import DB_CONFIG


app = Flask(__name__)

# Session secret key
app.secret_key = "wellness-center-secret-key"


# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_db_connection():

    return mysql.connector.connect(**DB_CONFIG)


# ==========================================
# HOME / REGISTRATION PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("register.html")


# ==========================================
# REGISTRATION
# ==========================================

@app.route("/register", methods=["POST"])
def register():

    # Get form data

    name = request.form["name"].strip()
    email = request.form["email"].strip()
    phone = request.form["phone"].strip()
    gender = request.form["gender"]
    dob = request.form["dob"]
    address = request.form["address"].strip()

    password = request.form["password"]
    confirm_password = request.form["confirm_password"]


    # ======================================
    # BACKEND VALIDATION
    # ======================================

    if not name:
        return "Name is required!"

    if not email:
        return "Email is required!"


    # Mobile validation

    if len(phone) != 10 or not phone.isdigit():

        return "Invalid mobile number!"


    # Password validation

    if len(password) < 8:

        return "Password must contain at least 8 characters!"


    # Confirm password

    if password != confirm_password:

        return "Password and Confirm Password do not match!"


    # ======================================
    # PASSWORD HASH
    # ======================================

    hashed_password = generate_password_hash(password)


    # ======================================
    # DATABASE CONNECTION
    # ======================================

    connection = get_db_connection()

    cursor = connection.cursor()


    # ======================================
    # INSERT QUERY
    # ======================================

    query = """
        INSERT INTO registrations
        (
            name,
            email,
            phone,
            gender,
            dob,
            address,
            password
        )

        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """


    values = (
        name,
        email,
        phone,
        gender,
        dob,
        address,
        hashed_password
    )


    try:

        cursor.execute(query, values)

        connection.commit()


        # Success page

        return render_template(
            "success.html",
            name=name
        )


    except mysql.connector.IntegrityError:

        return "Email already registered!"


    finally:

        cursor.close()

        connection.close()


# ==========================================
# ADMIN DASHBOARD
# ==========================================

@app.route("/admin/")
def admin():

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
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
        ORDER BY id ASC
    """

    cursor.execute(query)

    registrations = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "admin.html",
        registrations=registrations
    )

# ==========================================
# ADMIN LOGIN
# ==========================================

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    # GET request

    if request.method == "GET":

        return render_template("admin_login.html")


    # POST request

    username = request.form["username"]
    password = request.form["password"]


    # Temporary admin credentials

    if username == "admin" and password == "admin123":

        session["admin_logged_in"] = True

        return redirect(url_for("admin"))


    return render_template(
        "admin_login.html",
        error="Invalid username or password!"
    )


# ==========================================
# ADMIN LOGOUT
# ==========================================

@app.route("/admin/logout")
def admin_logout():

    session.pop("admin_logged_in", None)

    return redirect(url_for("admin_login"))


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)