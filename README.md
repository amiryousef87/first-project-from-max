First Project from Max

A modern Flask-based website built by Max, designed with clean UI, fast performance, and practical Python web development in mind. This project demonstrates a structured Flask app with templates, static files, and modular routing.

Overview

This project provides a professional example of a simple but extensible web application using Flask and Tailwind CSS.
It includes multiple pages: homepage, about page, project showcase, and a contact form.

Technologies Used

Python 3.10+

Flask

Jinja2 Templates

Tailwind CSS

HTML5 / CSS3

Gunicorn (for production deployment)

Installation

Follow these steps to run the project locally:

Clone the repository

git clone https://github.com/YOUR_USERNAME/first-project-from-max.git
cd first-project-from-max


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux


Install dependencies

pip install -r requirements.txt
pip install flask-babel

Running the Application

Development server:

python app.py
flask run


Open your browser at http://127.0.0.1:5000

Production (with Gunicorn):

gunicorn app:app

Screenshots

Home
<img width="800" src="https://github.com/user-attachments/assets/e6463bea-bd9c-4d24-8dad-1bf04717c796" />

About
<img width="800" src="https://github.com/user-attachments/assets/6753e4a7-4e95-4de0-b67e-6c4e7521df7d" />

Projects
<img width="800" src="https://github.com/user-attachments/assets/36e84fdf-2497-482b-87aa-4b721072de5e" />

Contact
<img width="800" src="https://github.com/user-attachments/assets/cef2272b-c6e1-40a3-b1b2-a4b27c34b87c" />
