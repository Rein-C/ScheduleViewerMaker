# ScheduleViewerMaker

---

# Flask Website Setup Guide

This guide will walk you through the process of setting up and running a Flask-based website on your local machine after downloading and extracting the ZIP file.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package installer)

## Step 1: Extract the ZIP File

Extract the downloaded ZIP file to a directory of your choice.

## Step 2: Open the Terminal

Open a terminal or command prompt and navigate to the directory where you extracted the ZIP file.

### On Windows:

```bash
cd path\to\your\extracted\folder
```

### On macOS/Linux:

```bash
cd path/to/your/extracted/folder
```

## Step 3: Install Dependencies

Install the required Python packages using the `requirements.txt` file provided in the repository:

```bash
pip install -r requirements.txt
```

## Step 4: Configure the Application

The application uses a `config.py` file for configuration. This file is already provided in the repository. Ensure that the `config.py` file is correctly set up with the necessary configurations.

### Example `config.py`:

```python
import os

SECRET_KEY = os.urandom(32)
SQLALCHEMY_DATABASE_URI = 'sqlite:///schedule_viewer.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## Step 5: Initialize the Database

If your application uses a database, you may need to initialize it. For example, if you are using Flask-SQLAlchemy and Flask-Migrate:

```bash
flask db init
flask db migrate
flask db upgrade
```

## Step 6: Run the Application

Start the Flask development server:

```bash
flask run
```

By default, Flask will run the application on `http://127.0.0.1:5000/`. Open this URL in your web browser to view your application.

## Step 7: Access the Application

You should now be able to access your Flask application by navigating to `http://127.0.0.1:5000/` in your web browser.

### Application Routes

- **Home Page:** `http://127.0.0.1:5000/`
- **Login Page:** `http://127.0.0.1:5000/login`
- **Signup Page:** `http://127.0.0.1:5000/signup`
- **Schedule Page:** `http://127.0.0.1:5000/schedule` (requires login)
- **Logout:** `http://127.0.0.1:5000/logout` (requires login)

## Troubleshooting

If you encounter any issues, here are a few common problems and their solutions:

- **Missing Dependencies:** Double-check the `requirements.txt` file and ensure all packages are listed correctly.
- **Database Issues:** Ensure the database URI is correct and that the database file exists (if using SQLite).

## Conclusion

Congratulations! You have successfully set up and run your Flask-based website. Feel free to explore and modify the application as needed.

---



## Versions 1,2 and 3 are available, with key differences regarding:

## V1 
![alttext](https://github.com/Rein-C/ScheduleViewerMaker/blob/main/Schedule%20Maker%20V1.png)
Subject Schedule details:

Subject Name ✔

Class Section ✔

Professor Name ✔

Day/s of the Week ✖

Time duration ✔, but maybe needs revision (supposed to be a drop down selection of class hours for beginning and end)

Room Number ✖

## V2
![alttext](https://github.com/Rein-C/ScheduleViewerMaker/blob/main/Schedule%20Maker%20V2.png)
Subject Schedule details:

Subject Name ✔

Class Section ✔

Professor Name ✔

Day/s of the Week ✔

Time duration ✔, but maybe needs revision (supposed to be a drop down selection of class hours for beginning and end)

Room Number ✔

##V3
![alttext](https://github.com/Rein-C/ScheduleViewerMaker/blob/main/Schedule%20Maker%20V3.png)
Subject Schedule details:

Subject Name ✔

Class Section ✔

Professor Name ✔

Day/s of the Week ✔ (revised, multiple days can now be manually selected)

Time duration ✔

Room Number ✔
