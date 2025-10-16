# First Project from Max

A production-minded Flask application starter with a multilingual public site, admin-style dashboard, and integrated AI tools.

This repository demonstrates a pragmatic Flask setup including authentication, file uploads, server-side charts, an AI page, and a small dashboard for managing projects and certificates.

---

## Contents

- `app.py` — main Flask application (routes, models, upload handlers)
- `templates/` — Jinja2 templates for pages and dashboard
- `static/` — CSS, JS, images, and upload folders (`static/uploads/...`)
- `requirements.txt` — Python dependencies

---

## Key Features

### Core
- User authentication (Flask-Login)
- Profile pictures (avatar) and profile fields (family name, phone)
- DB-backed projects with ZIP upload and delete
- Certificates upload and listing
- Server-side charts (PNG & SVG) generated with matplotlib
- Internationalization support via Flask-Babel

### New: AI Page
- `/ai` — A dedicated AI Hub page
- Interactive sections for:
  - AI Chat Assistant
  - AI Image Generator
  - AI Code Assistant
- Designed with TailwindCSS for a modern, gradient-based layout
- Ready for integration with OpenAI or local AI APIs

---

## Prerequisites

- Python 3.8+ installed  
- Recommended: use a virtual environment (`venv`)

---

## Installation (Windows)

1. Clone the repository and change directory:
   ```powershell
   git clone https://github.com/amiryousef87/first-project-from-max.git
   cd first-project-from-max
   ```

2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

---

## Running the App (Development)

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

**Notes**
- On first run, the app creates the SQLite database `users.db` and seeds a default admin user (`admin` / `123456`) for development.
- If you encounter import errors, ensure your virtual environment is active and dependencies are installed.

---

## Important Routes

### Public Pages
- `/` — Home  
- `/about`, `/contact` — Informational pages  
- `/projects` — Public project listing  
- `/video` — Example videos  
- `/ai` — Artificial Intelligence Hub  

### Dashboard (Login Required)
- `/login` — Login / Register  
- `/dashboard` — Main dashboard  
- `/dashboard/projects` — Manage projects (add/delete)  
- `/certificates` — Upload/list certificates  
- `/profile` — Update avatar, family name, phone  
- `/charts` — Server-rendered charts  

---

## Uploads and Storage

Upload folders under `static/uploads/`:
- Projects: `static/uploads/projects/`
- Certificates: `static/uploads/certificates/`
- Avatars: `static/uploads/avatars/`

Ensure these directories exist and are writable by the app.

---

## Database & Migrations

- SQLite database: `sqlite:///users.db`
- A built-in helper adds missing columns (e.g. `avatar`, `family_name`, `project_file`) automatically.
- For production, consider using Alembic for explicit migrations.

---

## Security & Deployment Notes

- Replace `app.secret_key` in `app.py` with a strong secret key for production.
- Disable `debug=True` in production.
- Deploy using Gunicorn + Nginx.
- Always validate and sanitize uploaded files.

---

## Development Tips

- To reset the DB: delete `users.db` and restart the app.
- Clear browser cache (Ctrl+F5) after editing CSS/templates.
- Log in using the default admin credentials for dashboard access.

---

## AI Integration Ideas

The `/ai` page is ready for:
- Chatbot integration with GPT APIs
- AI image generation endpoints
- Code analysis and completion modules
- Flask REST API connection to local or cloud AI services

You can extend `ai.html` and add Flask routes to connect to your preferred AI backend.

---

## Contributing

Contributions are welcome.  
If you add new routes or features (e.g. new AI tools), update this README accordingly.

---

## License

MIT License  
© 2025 Amiryousef Tousi
