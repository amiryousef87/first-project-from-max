# 🚀 First Project from Max

A production-ready **Flask** application starter with a multilingual public site, admin dashboard, and integrated AI tools.

This repository demonstrates a pragmatic Flask setup including authentication, file uploads, server-side charts, an AI page, and a dashboard for managing projects and certificates.

---

## 📂 Contents

- `app.py` — Main Flask application (routes, models, upload handlers)
- `templates/` — Jinja2 templates for pages and dashboard
- `static/` — CSS, JS, images, and upload folders (`static/uploads/...`)
- `requirements.txt` — Python dependencies

---

## ✨ Key Features

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

## ⚙️ Prerequisites

- Python 3.8+
- Recommended: use a virtual environment (`venv`)

---

## 💻 Installation (Windows)

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


## 📜 License

**MIT License**  
© 2025  A . F . T

