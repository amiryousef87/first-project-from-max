
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
# first-project-from-max — updated README

A compact Flask dashboard demo (multilingual-ready) with server-side charts, file uploads and a small projects & certificates dashboard.

This README highlights how to run the app locally and where to find important features added since the original project scaffold.

---

## Quick start (Windows)

1. Clone the repo and enter the folder:

```powershell
git clone https://github.com/amiryousef87/first-project-from-max.git
cd first-project-from-max
```

2. Create and activate a virtualenv (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run in development mode:

```powershell
python app.py
# open http://127.0.0.1:5000 in your browser
```

Notes:
- The project uses Flask, Flask-Login, Flask-Babel, and SQLAlchemy. If you hit import errors, ensure the environment is activated and `pip install -r requirements.txt` finished successfully.

---

## What changed / useful routes

- Dashboard (admin-style): `/dashboard` — main dashboard page
- Projects (DB-backed dashboard): `/dashboard/projects` — add/delete projects (uploads saved to `static/uploads/projects`)
- Certificates: `/certificates` — upload and list certificate files (saved to `static/uploads/certificates`)
- Server-side charts: `/chart/<name>.png` and `/chart/<name>.svg`

Admin seed user (created on first run): username `admin` / password `123456` (for development convenience).

---

## File uploads

- Project ZIPs: saved to `static/uploads/projects/` and referenced from project cards
- Certificates: saved to `static/uploads/certificates/`

Make sure `static/uploads/projects` and `static/uploads/certificates` exist and are writable by the app.

---

## Database notes

- SQLite is used by default (e.g. `sqlite:///users.db`).
- A small migration helper in `app.py` will add the `project_file` column to the `project` table if it's missing (runs at startup).

If you run into `sqlite3.OperationalError: no such column: project.project_file`, restart the app after ensuring `app.py` has the migration helper and the app will add the column automatically.

---

## CSS and templates

- The projects and certificates views use `static/css/projects-dashboard.css`. If you customize the stylesheet, reload your browser (Ctrl+F5) to clear cached CSS.
- Templates of interest: `templates/projects_dashboard.html`, `templates/certificate.html`, `templates/dashboard.html` and `templates/base.html`.

---

## Troubleshooting

- Missing packages: ensure virtualenv is active and `pip install -r requirements.txt` completed.
- Permission errors on upload: check the static/uploads directory permissions.
- Routes not found/templates: confirm templates exist under `templates/` and that you are visiting the dashboard routes (some pages are dashboard-only and require login).

---

## Contributing

PRs and issues welcome. If you change routes or uploads paths, please update this README.

---

## License

MIT
