
# first-project-from-max

## Modern Flask Web Application with Multilingual Support and Dashboard  
**Beautiful • Fast • Scalable**

A clean, lightweight, and multilingual-ready Flask application — perfect for modern web development and UI prototyping.

---

## Overview

**first-project-from-max** is a modern, extensible Flask-based web application. It’s designed with clean architecture, internationalization (i18n), and a responsive Tailwind CSS UI.

This project demonstrates:

- How to structure a scalable Flask application  
- Efficient use of Jinja2 templates with inheritance  
- Integration of Flask-Babel for multilingual support  
- Building a modern dashboard using Flask and TailwindCSS  

---

## Key Features

### Core Functionality
- Organized and modular Flask structure  
- Jinja2 templating with base inheritance  
- Multilingual support via Flask-Babel (English, Persian, etc.)  
- Dynamic project pages with JSON & Flask API endpoints  
- Integrated Dashboard Page (`dashboard.html`)  

### User Interface
- TailwindCSS 3 for fast, utility-first styling  
- Responsive layout (mobile to desktop)  
- Smooth gradients and clean typography  
- Minimalistic, modern design  

---

## Tech Stack

| Layer | Technology | Description |
|--------|-------------|-------------|
| Backend | Flask 2.3+ | Python micro web framework |
| Templating | Jinja2 | HTML rendering with logic |
| Frontend | TailwindCSS 3+ | Modern, responsive CSS framework |
| Localization | Flask-Babel | Multi-language support |
| Deployment | Gunicorn / Nginx | Production-ready WSGI setup |

---

## Installation & Setup

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/amiryousef87/first-project-from-max.git
cd first-project-from-max
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# If Flask-Babel is missing:
# pip install flask-babel
```

### 4. Run the Application

**Development Mode:**

```bash
python app.py
# or
flask run
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

**Production Mode:**

```bash
gunicorn app:app
```

---

## Project Structure

```
first-project-from-max/
├── app.py              # Main Flask application file
├── config.py           # Configuration file (languages, settings)
├── requirements.txt    # Project dependencies
├── /templates          # HTML templates
│   ├── base.html       # Base template for inheritance
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── contact.html
│   └── dashboard.html  # Dedicated dashboard page
└── /static             # Static files (CSS, JS, Images)
```

---

## Localization (Flask-Babel)

The application supports multiple languages via **Flask-Babel**.

Languages are defined in `config.py` under the `LANGUAGES` variable:

```python
LANGUAGES = ['en', 'fa']
```

Users can switch languages by appending the `?lang=` parameter to the URL:

Example:  
[http://127.0.0.1:5000/?lang=fa](http://127.0.0.1:5000/?lang=fa)

---

## Dashboard Page

The `dashboard.html` file demonstrates:

- Dynamic data rendering with Jinja2  
- A clean, responsive design using TailwindCSS  
- Full integration with Flask routes and application logic  

---

## Contributing

Contributions, issues, and feature requests are welcome.  
Feel free to check the issues page or submit a Pull Request.

---

## License

This project is licensed under the MIT License.
