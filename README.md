#  First Project from Max

A production-ready **Flask** application starter with a multilingual public site, admin dashboard, and integrated AI tools.

This repository demonstrates a pragmatic Flask setup including authentication, file uploads, server-side charts, an AI page, and a dashboard for managing projects and certificates.

---

##  Contents

- `app.py` — Main Flask application (routes, models, upload handlers)
- `templates/` — Jinja2 templates for pages and dashboard
- `static/` — CSS, JS, images, and upload folders (`static/uploads/...`)
- `requirements.txt` — Python dependencies

---

##  Key Features

### Core

- User authentication (`Flask-Login`)
- Profile pictures (avatars) and extra fields (family name, phone)
- Projects with ZIP upload and delete
- Certificate upload & listing
- Server-side charts (PNG & SVG) with `matplotlib`
- Multilingual support via `Flask-Babel`

### AI Hub (`/ai`)

- **Chat Assistant**
- **Image Generator**
- **Code Assistant**
- Modern gradient layout powered by **TailwindCSS**
- Ready for integration with OpenAI or local AI APIs

---

##  Prerequisites

- Python 3.8+
- Recommended: use a virtual environment (`venv`)

---

##  Installation (Windows)

1. Clone the repo:

```powershell
git clone https://github.com/amiryousef87/first-project-from-max.git
cd first-project-from-max
```

2. Create & activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

---

##  Running the App (Development)

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

**Notes:**

- First run creates SQLite DB `users.db` and seeds default admin: `admin / 123456`
- Make sure the virtual environment is active if import errors occur

---

##  Important Routes

### Public Pages

- `/` — Home
- `/about` / `/contact` — Info pages
- `/projects` — Public project listing
- `/video` — Example videos
- `/ai` — AI Hub

### Dashboard (Login Required)

- `/login` — Login / Register
- `/dashboard` — Main dashboard
- `/dashboard/projects` — Manage projects
- `/certificates` — Upload/list certificates
- `/profile` — Update avatar, family name, phone
- `/charts` — Server-rendered charts

---

##  Uploads & Storage

Folders under `static/uploads/`:

- `projects/` — Project files
- `certificates/` — Certificates
- `avatars/` — Profile images

> Make sure these directories exist and are writable.

---

##  Database & Migrations

- SQLite DB: `sqlite:///users.db`
- Auto-adds missing columns (avatar, family_name, project_file)
- For production, consider **Alembic** for explicit migrations

---

##  Security & Deployment

- Replace `app.secret_key` with a strong key for production
- Disable `debug=True` in production
- Deploy with **Gunicorn + Nginx**
- Always validate uploaded files

---

##  Development Tips

- Reset DB: delete `users.db` and restart app
- Clear browser cache after template/CSS changes
- Default admin credentials available for dashboard login

---

##  AI Integration Ideas

The `/ai` page can support:

- GPT-based chatbot
- AI image generation
- Code analysis & completion
- REST API connection to local or cloud AI services

Extend `ai.html` and Flask routes to connect to your AI backend.

---

##  Contributing

Contributions welcome!  
If you add new routes or AI features, update this README accordingly.

---

##  License

**MIT License**  
© 2025 Amiryousef Tousi
