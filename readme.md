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
