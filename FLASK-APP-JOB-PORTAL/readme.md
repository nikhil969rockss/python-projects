# Step 1
# 🌐 Flask Starter Web Application

Simple Flask-based web application that renders an HTML template.

---

# 📌 Project Overview

This is a minimal Flask web application that:

- Creates a web server using Flask
- Defines a single route (`/`)
- Renders an HTML template (`index.html`)
- Runs on port 5000 in debug mode

This project demonstrates:

- Flask routing
- Template rendering
- Basic project structure
- Development server setup

---

# 📂 Project Structure

```
project/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

⚠ Important:  
Flask requires a `templates` folder to render HTML files.

---

# 🧰 Requirements

## Install Flask

```bash
pip install flask
```

Check installation:

```bash
pip show flask
```

---

# 🧠 Application Code Explanation

## 1️⃣ Import Required Modules

```python
from flask import Flask
from flask import render_template
```

### Explanation

- `Flask` → Main application class
- `render_template` → Used to render HTML files

---

## 2️⃣ Create Flask App Instance

```python
app = Flask(__name__)
```

- `__name__` tells Flask where the application is located
- Required to initialize the app

---

## 3️⃣ Define Route

```python
@app.route("/")
```

This decorator:

- Maps URL `/` (home page)
- To the function below it

---

## 4️⃣ Home Page Function

```python
def home_page():
    return render_template("index.html")
```

### What Happens Here?

- When user visits `http://127.0.0.1:5000/`
- Flask calls `home_page()`
- It renders `index.html` from templates folder

---

## 5️⃣ Run the Application

```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### Explanation

- `debug=True`
  - Enables auto reload
  - Shows error stack trace in browser

- `port=5000`
  - App runs on port 5000

App URL:
```
http://127.0.0.1:5000/
```

---

# 🖥️ How to Run the Project

## Step 1

Navigate to project directory:

```bash
cd project
```

## Step 2

Run the app:

```bash
python app.py
```

OR (Mac/Linux):

```bash
python3 app.py
```

## Step 3

Open browser and visit:

```
http://127.0.0.1:5000/
```

---

# 📝 Sample index.html

Create file:

```
templates/index.html
```

Example content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Home</title>
</head>
<body>
    <h1>Welcome to Flask App 🚀</h1>
</body>
</html>
```

---

# 🏗 Concepts Used

- Flask Application Setup
- Routing
- Template Rendering
- Debug Mode
- Development Server

---
---
---

# Step 2
# 🌐 Flask Form Application  
Flask + SQLAlchemy + dotenv + Flash Messages

---

# 📌 Project Overview

This is a Flask-based web application that:

- Accepts form data from user
- Saves data into a database using SQLAlchemy
- Uses environment variables via dotenv
- Implements flash messages
- Handles database errors
- Uses application factory pattern

This project demonstrates:

- Flask routing
- POST form handling
- Database integration
- Environment variable security
- Error handling
- OOP structure

---

# 🏗 Project Structure

```
project/
│
├── app.py
├── .env
├── db/
│   └── database.py
├── models/
│   └── form.py
├── templates/
│   └── index.html
└── README.md
```

---

# 🧰 Requirements

Install dependencies:

```bash
pip install flask
pip install flask-sqlalchemy
pip install python-dotenv
```

---

# 🔐 Environment Variables (.env)

Create a `.env` file in root directory:

```
SECRET_KEY=your_secret_key_here
SQLALCHEMY_DATABASE_URI=sqlite:///form.db
```

### Why use .env?

- Protects sensitive data
- Keeps credentials outside source code
- Good production practice

---

# 🧠 Application Architecture

## 1️⃣ Load Environment Variables

```python
from dotenv import load_dotenv
load_dotenv()
```

Ensures environment variables are loaded before app starts.

---

## 2️⃣ Application Factory Pattern

```python
def create_app():
```

### Why use Factory Pattern?

- Scalable architecture
- Easy testing
- Clean separation of configuration

Inside factory:

```python
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
db.init_app(app)
```

---

# 🌐 Home Route

```python
@app.route("/", methods=['GET', 'POST'])
```

This route:

- Renders form page (GET)
- Processes form submission (POST)

---

# 📝 Form Submission Flow

When method == POST:

### 1️⃣ Get Form Data

```python
first_name = request.form['first_name']
```

---

### 2️⃣ Convert Date

```python
date_f = datetime.strptime(date, '%Y-%m-%d')
```

Converts string → Python datetime object.

---

### 3️⃣ Create Model Object

```python
form = Form(
    first_name=first_name,
    last_name=last_name,
    email=email,
    date=date_f,
    occupation=occupation
)
```

---

### 4️⃣ Add to Database Session

```python
db.session.add(form)
```

---

### 5️⃣ Commit Changes

```python
db.session.commit()
```

---

# ⚠️ Error Handling

## IntegrityError

```python
except IntegrityError:
```

Occurs when:

- Email already exists (unique constraint)

Actions:

- Rollback transaction
- Flash error message

---

## OperationalError

```python
except OperationalError:
```

Occurs when:

- Database connection issue
- Table missing

---

# 💬 Flash Messages

```python
flash('Your Form has been submitted', 'success')
```

Flash categories used:

- success
- error

Used to display feedback in HTML.

---

# 🗄 Database Setup

Inside main block:

```python
with app.app_context():
    db.create_all()
```

### What does this do?

- Creates database tables
- Must run inside application context

---

# 🚀 How to Run the Application

## Step 1

Navigate to project directory:

```bash
cd project
```

## Step 2

Create .env file

## Step 3

Run the app:

```bash
python app.py
```

## Step 4

Open browser:

```
http://127.0.0.1:5000/
```

---

# 🏗 Concepts Used

- Flask Routing
- POST Request Handling
- SQLAlchemy ORM
- Flash Messaging
- Environment Variables
- Error Handling
- Application Factory Pattern
- Database Transactions

---

# 🔁 Execution Flow

1. App starts
2. Environment variables loaded
3. Database initialized
4. User opens homepage
5. User submits form
6. Data validated
7. Data inserted into DB
8. Success/Error message displayed

---

# 📌 Future Improvements

- Add form validation (Flask-WTF)
- Add CSRF protection
- Add email sending after submission
- Add admin dashboard
- Add pagination
- Convert into Blueprint structure
- Add REST API endpoints
- Add authentication system
- Deploy using Gunicorn + Nginx

---

# 🔒 Security Considerations

- Always use strong SECRET_KEY
- Do not commit .env file
- Use PostgreSQL in production
- Disable debug mode in production

---

# ✅ Conclusion

This project demonstrates a production-style Flask architecture using:

- Application Factory Pattern
- SQLAlchemy ORM
- dotenv configuration
- Proper error handling

It is a strong foundation for building scalable web applications.

# Email sending With the App
# 🌐 Flask Job Portal Application  
Flask + SQLAlchemy + dotenv + Flash + Email Notification

---

# 📌 Project Overview

This is an enhanced version of the Flask Form Application.

### New Feature Added ✅
- Automatic email confirmation after successful registration

The application now:

- Accepts user form data
- Stores data in database
- Handles duplicate emails
- Sends confirmation email
- Uses environment variables for security
- Implements application factory pattern
- Uses proper transaction handling

---

# 🏗 Project Structure

```
project/
│
├── app.py
├── .env
├── db/
│   └── database.py
├── models/
│   └── form.py
├── templates/
│   └── index.html
└── README.md
```

---

# 🧰 Requirements

Install dependencies:

```bash
pip install flask
pip install flask-sqlalchemy
pip install python-dotenv
pip install flask-mail
```

---

# 🔐 Environment Variables (.env)

Create a `.env` file in root directory:

```
SECRET_KEY=your_secret_key_here
SQLALCHEMY_DATABASE_URI=sqlite:///form.db
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
```

⚠ For Gmail:
- Enable 2-Step Verification
- Generate App Password
- Use App Password in `.env`

---

# 🧠 New Feature: Email Confirmation

## 📧 Mail Configuration

Inside `create_app()`:

```python
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv('SENDER_EMAIL')
app.config["MAIL_PASSWORD"] = os.getenv('APP_PASSWORD')
```

Mail instance:

```python
mail = Mail()
mail.init_app(app)
```

---

# 📝 Updated Form Submission Flow

When user submits form:

## 1️⃣ Save Data to Database

```python
db.session.add(form)
db.session.commit()
```

---

## 2️⃣ Create Email Message

```python
message = Message(
    subject="Job Portal Registeration",
    sender=app.config['MAIL_USERNAME'],
    recipients=[email],
    body=message_body
)
```

---

## 3️⃣ Send Email

```python
mail.send(message)
```

---

## 4️⃣ Flash Success Message

```python
flash('Your Form has been submitted', 'success')
```

---

## 5️⃣ Redirect After POST

```python
return redirect(url_for('home_page'))
```

### Why Redirect?

- Prevents form resubmission
- Avoids duplicate inserts on refresh
- Follows POST-Redirect-GET pattern

---

# ⚠️ Error Handling

## IntegrityError

Occurs when:

- Email already exists (unique constraint)

Handled by:

```python
db.session.rollback()
flash('This email is already registered','error')
```

---

## OperationalError

Occurs when:

- Database connection fails
- Table missing

---

# 🔁 Execution Flow (Updated)

1. User opens homepage
2. User submits form
3. Data validated
4. Data inserted into DB
5. Confirmation email sent
6. Success message flashed
7. User redirected to home page

---

# 🔒 Security Features

- SECRET_KEY protects session cookies
- Sensitive data stored in `.env`
- App Password used instead of Gmail password
- Database transaction rollback on failure

---

# 🚀 How to Run

## Step 1

Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## Step 2

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3

Create `.env` file

---

## Step 4

Run application

```bash
python app.py
```

---

Open browser:

```
http://127.0.0.1:5000/
```

---

# 🏗 Concepts Used

- Flask Routing
- Application Factory Pattern
- SQLAlchemy ORM
- Database Transactions
- Flash Messaging
- Flask-Mail
- Environment Variables
- POST-Redirect-GET Pattern
- Exception Handling

---

# 📌 Future Enhancements

- Add Flask-WTF validation
- Add HTML email templates
- Add email verification token
- Add user authentication system
- Convert to Blueprint architecture
- Add logging system
- Deploy using Gunicorn + Nginx
- Add Celery for async email sending
- Add rate limiting
- Add REST API endpoints

---

# 🏆 What This Project Demonstrates

This is no longer a beginner Flask project.

It now demonstrates:

- Production-style configuration
- Secure environment handling
- Email integration
- Database integrity handling
- Clean architecture design

---

# ✅ Conclusion

This project shows how to build a:

✔ Secure  
✔ Database-driven  
✔ Email-enabled  
✔ Production-ready Flask application  

It is a solid foundation for building:

- Job portal systems
- Registration systems
- CRM applications
- SaaS backend systems