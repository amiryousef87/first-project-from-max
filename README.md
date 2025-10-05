# first-project-from-max


# First Project from Max

This project is a modern Flask-based website built by Max, focused on clean design, speed, and practical web development using Python and Flask. It demonstrates how to create a well-structured web app with templates, static files, and modular routing.

---

## Overview

The purpose of this project is to provide a professional example of a simple but extensible web application using Flask and Tailwind CSS.  
It includes multiple pages such as the homepage, about page, project showcase, and a contact form.

---

## Technologies Used

- Python 3.10+
- Flask
- Jinja2 Templates
- Tailwind CSS
- HTML5 / CSS3
- Gunicorn (for production deployment)

---

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/first-project-from-max.git
   cd first-project-from-max
Create and activate a virtual environment (recommended):

bash
Copy code
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
To start the Flask development server:

bash
Copy code
python app.py
Once the server starts, open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
For production, use Gunicorn:

bash
Copy code
gunicorn app:app