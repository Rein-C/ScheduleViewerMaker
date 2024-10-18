# ScheduleViewerMaker

---

# Flask Website Setup Guide

This guide will walk you through the process of setting up and running a Flask-based website on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/installing/) (Python package installer)
- [Git](https://git-scm.com/downloads) (optional, for cloning the repository)

## Step 1: Clone the Repository

If you haven't already cloned the repository, you can do so using Git:

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

## Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment:

### On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

Install the required Python packages using the `requirements.txt` file provided in the repository:

```bash
pip install -r requirements.txt
```

## Step 4: Configure the Application

Depending on your application, you may need to configure environment variables or settings. Typically, this involves creating a `.env` file or setting up a configuration file.

### Example `.env` File:

```plaintext
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URI=sqlite:///yourdatabase.db
```

### Load Environment Variables:

If you are using a `.env` file, you can load it using the `python-dotenv` package:

```bash
pip install python-dotenv
```

Then, in your `app.py` or `__init__.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URI = os.getenv('DATABASE_URI')
```

## Step 5: Initialize the Database (if applicable)

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

## Troubleshooting

If you encounter any issues, here are a few common problems and their solutions:

- **Virtual Environment Not Activating:** Ensure you are in the correct directory and that the virtual environment was created successfully.
- **Missing Dependencies:** Double-check the `requirements.txt` file and ensure all packages are listed correctly.
- **Database Issues:** Ensure the database URI is correct and that the database file exists (if using SQLite).

## Conclusion

Congratulations! You have successfully set up and run your Flask-based website. Feel free to explore and modify the application as needed.

---



## Versions 1 and 2 are available, with key differences regarding:

V1 
![alttext](https://github.com/Rein-C/ScheduleViewerMaker/blob/main/Schedule%20Maker%20V1.png)
Subject Schedule details:

Subject Name ✔

Class Section ✔

Professor Name ✔

Day/s of the Week ✖

Time duration ✔, but maybe needs revision (supposed to be a drop down selection of class hours for beginning and end)

Room Number ✖

V2
![alttext](https://github.com/Rein-C/ScheduleViewerMaker/blob/main/Schedule%20Maker%20V2.png)
Subject Schedule details:

Subject Name ✔

Class Section ✔

Professor Name ✔

Day/s of the Week ✔

Time duration ✔, but maybe needs revision (supposed to be a drop down selection of class hours for beginning and end)

Room Number ✔
