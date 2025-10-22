import matplotlib.pyplot as plt
import os
from io import BytesIO
import re
import logging

from flask import Flask, render_template, redirect, url_for, request, flash, Response, jsonify
from flask_babel import Babel, gettext as _
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
    UserMixin,
)
from flask_migrate import Migrate
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename, safe_join
from models import db, Project, Product, User

import numpy as np
import matplotlib

matplotlib.use("Agg")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates"),
)
app.secret_key = "your_secret_key_here"

UPLOAD_FOLDER = 'uploads'

# مطمئن شو پوشه وجود دارد
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Upload configuration for project zip files
UPLOAD_RELATIVE = os.path.join("uploads", "projects")
UPLOAD_FOLDER = os.path.join(app.static_folder, "uploads", "projects")
ALLOWED_EXTENSIONS = {".zip"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Certificates upload folder
CERT_UPLOAD_REL = os.path.join("uploads", "certificates")
CERT_UPLOAD_FOLDER = os.path.join(app.static_folder, "uploads", "certificates")
CERT_ALLOWED_EXT = {".pdf", ".png", ".jpg", ".jpeg"}
if not os.path.exists(CERT_UPLOAD_FOLDER):
    os.makedirs(CERT_UPLOAD_FOLDER, exist_ok=True)

# Avatar upload folder (user profile pictures)
AVATAR_REL = os.path.join("uploads", "avatars")
AVATAR_UPLOAD_FOLDER = os.path.join(app.static_folder, "uploads", "avatars")
AVATAR_ALLOWED_EXT = {".png", ".jpg", ".jpeg", ".gif"}
if not os.path.exists(AVATAR_UPLOAD_FOLDER):
    os.makedirs(AVATAR_UPLOAD_FOLDER, exist_ok=True)

# دیتابیس SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# مدیریت لاگین
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Babel برای چند زبانه بودن
app.config["LANGUAGES"] = ["en", "fa"]


# تنظیم فایل لاگ
logging.basicConfig(
    filename='system.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S'
)

# لاگ کردن هر درخواست


@app.before_request
def log_request_info():
    logging.info(
        f'{request.remote_addr} "{request.method} {request.path} {request.environ.get("SERVER_PROTOCOL")}"')


def select_locale():
    lang = request.args.get("lang")
    if lang and lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=select_locale)


@app.context_processor
def inject_direction():
    lang = select_locale()
    return {"current_lang": lang, "dir": "rtl" if lang == "fa" else "ltr"}





# Project model for dashboard-managed projects



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# صفحات عمومی
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/shop")
def shop():
    products = Product.query.all()
    return render_template("shop.html")
    # , products=products


@app.route("/users")
@login_required
def users():
    return render_template("users.html")


@app.route("/setting")
@login_required
def setting():
    return render_template("setting.html", user=current_user)


@app.route("/projects")
def projects():
    projects_list = Project.query.all()
    return render_template("projects.html", projects=projects_list)


@app.route("/dashboard/projects")
@login_required
def projects_dashboard():
    # Use DB-backed projects for the dashboard. Show all projects stored in DB.
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template("projects_dashboard.html", projects=projects)


@app.route("/tasks")
@login_required
def tasks():
    return render_template("tasks.html", user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/videos")
def videos():
    # templates contain `video.html` (singular) so render that to avoid TemplateNotFound
    return render_template("video.html")


@app.route("/courses")
@login_required
def courses():
    return render_template("courses.html", user=current_user)


@app.route("/charts")
@login_required
def charts():
    return render_template("charts.html", user=current_user)


@app.route("/ai")
def ai():
    return render_template("ai.html", user=current_user)


@app.route("/api/logs")
@login_required
def get_logs():
    try:
        with open('system.log', 'r', encoding='utf-8', errors='ignore') as f:
            logs = f.readlines()[-50:]
    except FileNotFoundError:
        logs = ["No log file found."]
    return jsonify(logs)


@app.route("/admin")
@login_required
def admin():
    try:
        with open('system.log', 'r', encoding='utf-8', errors='ignore') as f:
            logs = f.readlines()[-20:]
    except FileNotFoundError:
        logs = ["No log file found."]
    users = User.query.all()
    return render_template("admin.html", users=users, current_user=current_user, logs=logs)



@app.route("/dashboard/projects/add", methods=["POST"])
@login_required
def add_project():
    title = request.form.get("title")
    desc = request.form.get("desc")
    tech = request.form.get("tech")
    # Handle uploaded zip file (optional)
    project_file = request.files.get("project_file")
    saved_filename = None
    if project_file and project_file.filename:
        filename = secure_filename(project_file.filename)
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            flash(_("Only .zip files are allowed for project uploads."), "danger")
            return redirect(url_for("projects_dashboard"))
        # make filename unique
        import time

        unique_name = f"{int(time.time())}_{filename}"
        dest_path = os.path.join(UPLOAD_FOLDER, unique_name)
        project_file.save(dest_path)
        saved_filename = unique_name
    if not title:
        flash(_("Title is required"), "danger")
        return redirect(url_for("projects_dashboard"))
    p = Project(title=title, desc=desc, tech=tech, project_file=saved_filename)
    db.session.add(p)
    db.session.commit()
    flash(_("Project added"), "success")
    return redirect(url_for("projects_dashboard"))


@app.route("/dashboard/projects/delete/<int:project_id>", methods=["POST"])
@login_required
def delete_project(project_id):
    p = Project.query.get_or_404(project_id)
    # remove uploaded file if exists
    if p.project_file:
        try:
            path = os.path.join(UPLOAD_FOLDER, p.project_file)
            if os.path.exists(path):
                os.remove(path)
        except Exception:
            pass
    db.session.delete(p)
    db.session.commit()
    flash(_("Project deleted"), "success")
    return redirect(url_for("projects_dashboard"))


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('video')
    if file:
        file.save(f"uploads/{file.filename}")  # مسیر ذخیره فایل
        flash("Video uploaded successfully!")
    return redirect(url_for('videos'))


@app.route("/certificates", methods=["GET", "POST"])
@login_required
def certificates():
    # Handle upload when POST
    if request.method == "POST":
        cert_file = request.files.get("certificate")
        if cert_file and cert_file.filename:
            filename = secure_filename(cert_file.filename)
            ext = os.path.splitext(filename)[1].lower()
            if ext not in CERT_ALLOWED_EXT:
                flash(_("Only PDF/JPG/PNG allowed for certificates."), "danger")
                return redirect(url_for("certificates"))
            import time

            unique = f"{int(time.time())}_{filename}"
            cert_file.save(os.path.join(CERT_UPLOAD_FOLDER, unique))
            flash(_("Certificate uploaded"), "success")
            return redirect(url_for("certificates"))

    # List existing uploaded certificates
    certs = []
    try:
        certs = sorted(os.listdir(CERT_UPLOAD_FOLDER), reverse=True)
    except Exception:
        certs = []
    return render_template("certificate.html", user=current_user, certs=certs)


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    # Show user profile and allow avatar upload
    if request.method == "POST":
        # handle text fields as well
        family_name = request.form.get("family_name")
        phone = request.form.get("phone")
        if family_name is not None:
            current_user.family_name = family_name
        if phone is not None:
            current_user.phone = phone

        avatar_file = request.files.get("avatar")
        if avatar_file and avatar_file.filename:
            filename = secure_filename(avatar_file.filename)
            ext = os.path.splitext(filename)[1].lower()
            if ext not in AVATAR_ALLOWED_EXT:
                flash(_("Only image files are allowed (png/jpg/jpeg/gif)."), "danger")
                return redirect(url_for("profile"))
            import time

            unique = f"{int(time.time())}_{filename}"
            dest = os.path.join(AVATAR_UPLOAD_FOLDER, unique)
            avatar_file.save(dest)
            # remove old avatar if exists
            try:
                if current_user.avatar:
                    old = os.path.join(AVATAR_UPLOAD_FOLDER,
                                       current_user.avatar)
                    if os.path.exists(old):
                        os.remove(old)
            except Exception:
                pass
            # save new avatar filename in user record
            current_user.avatar = unique

        try:
            db.session.commit()
            flash(_("Profile updated."), "success")
        except Exception:
            flash(_("Could not update profile."), "danger")
        return redirect(url_for("profile"))
    return render_template("profile.html", user=current_user)


# Serve server-side generated charts as PNG images
@app.route("/chart/<chart_name>.png")
@login_required
def chart_png(chart_name):
    # Simple demo data - replace with real data as needed
    fig, ax = plt.subplots(figsize=(6, 3))
    if chart_name == "activity":
        x = np.arange(1, 15)
        y = np.random.randint(50, 200, size=x.shape)
        ax.plot(x, y, color="#0275d8", linewidth=2)
        ax.fill_between(x, y, color="#0275d8", alpha=0.2)
        ax.set_title("Activity (last 14 days)")
        ax.set_xlabel("Day")
        ax.set_ylabel("Visits")
    elif chart_name == "missions":
        labels = ["Completed", "Pending", "Failed"]
        sizes = [60, 30, 10]
        colors = ["#28a745", "#ffc107", "#dc3545"]
        ax.pie(sizes, labels=labels, colors=colors,
               autopct="%1.1f%%", startangle=140)
        ax.axis("equal")
        ax.set_title("Missions Today")
    else:
        ax.text(
            0.5,
            0.5,
            "Chart not found",
            horizontalalignment="center",
            verticalalignment="center",
        )

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=100)
    plt.close(fig)
    buf.seek(0)
    return app.response_class(buf.getvalue(), mimetype="image/png")


# Serve SVG (vector) charts generated by matplotlib
@app.route("/chart/<chart_name>.svg")
@login_required
def chart_svg(chart_name):
    fig, ax = plt.subplots(figsize=(6, 3))
    if chart_name == "activity":
        x = np.arange(1, 15)
        y = np.random.randint(50, 200, size=x.shape)
        ax.plot(x, y, color="#0275d8", linewidth=2)
        ax.fill_between(x, y, color="#0275d8", alpha=0.2)
        ax.set_title("Activity (last 14 days)")
        ax.set_xlabel("Day")
        ax.set_ylabel("Visits")
    elif chart_name == "missions":
        labels = ["Completed", "Pending", "Failed"]
        sizes = [60, 30, 10]
        colors = ["#28a745", "#ffc107", "#dc3545"]
        ax.pie(sizes, labels=labels, colors=colors,
               autopct="%1.1f%%", startangle=140)
        ax.axis("equal")
        ax.set_title("Missions Today")
    else:
        ax.text(
            0.5,
            0.5,
            "Chart not found",
            horizontalalignment="center",
            verticalalignment="center",
        )

    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="svg")
    plt.close(fig)
    buf.seek(0)
    return app.response_class(buf.getvalue(), mimetype="image/svg+xml")


# ثبت‌نام
@app.route("/register", methods=["GET", "POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    family_name = request.form.get("family_name")
    phone = request.form.get("phone")
    password = request.form.get("password")

    if User.query.filter_by(username=username).first():
        flash(_("Username already exists!"), "danger")
        return redirect(url_for("login"))
    if User.query.filter_by(email=email).first():
        flash(_("Email already exists!"), "danger")
        return redirect(url_for("login"))

    new_user = User(
        username=username, email=email, family_name=family_name, phone=phone
    )
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    flash(_("Registered successfully! Please login."), "success")
    return redirect(url_for("login"))


# لاگین
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        family_name = request.form.get("family_name")
        phone = request.form.get("phone")
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            # if optional family_name/phone provided on login, save them to profile
            try:
                updated = False
                if family_name and (
                    not user.family_name or user.family_name != family_name
                ):
                    user.family_name = family_name
                    updated = True
                if phone and (not user.phone or user.phone != phone):
                    user.phone = phone
                    updated = True
                if updated:
                    db.session.commit()
            except Exception:
                pass
            next_page = request.args.get("next")
            return redirect(next_page or url_for("dashboard"))
        flash(_("Invalid username or password!"), "danger")
        return redirect(url_for("login"))
    return render_template("login.html")


# داشبورد
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


def ensure_project_file_column():
    try:
        with db.engine.begin() as conn:
            res = conn.execute(text("PRAGMA table_info('project')"))
            cols = [r[1] for r in res]
            if "project_file" not in cols:
                conn.execute(
                    text("ALTER TABLE project ADD COLUMN project_file VARCHAR(300)")
                )
    except Exception:
        pass


def ensure_user_avatar_column():
    try:
        with db.engine.begin() as conn:
            res = conn.execute(text("PRAGMA table_info('user')"))
            cols = [r[1] for r in res]
            if "avatar" not in cols:
                conn.execute(
                    text("ALTER TABLE user ADD COLUMN avatar VARCHAR(300)"))
    except Exception:
        pass


def ensure_user_contact_columns():
    try:
        with db.engine.begin() as conn:
            res = conn.execute(text("PRAGMA table_info('user')"))
            cols = [r[1] for r in res]
            if "family_name" not in cols:
                conn.execute(
                    text("ALTER TABLE user ADD COLUMN family_name VARCHAR(150)")
                )
            if "phone" not in cols:
                conn.execute(
                    text("ALTER TABLE user ADD COLUMN phone VARCHAR(50)"))
    except Exception:
        pass


with app.app_context():
    db.create_all()
    # Run safe migrations
    try:
        ensure_project_file_column()
    except Exception:
        pass
    try:
        ensure_user_avatar_column()
    except Exception:
        pass
    try:
        ensure_user_contact_columns()
    except Exception:
        pass

    # Create default admin if missing
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", email="admin@example.com")
        admin.set_password("123456")  # default admin password
        db.session.add(admin)
        db.session.commit()


# Serve minified CSS on-the-fly for local CSS files under static/css
@app.route("/minified_css/<path:filename>")
def minified_css(filename):
    # restrict to css directory and simple filenames
    try:
        # only allow files under static/css (use commonpath to handle Windows paths)
        css_dir = os.path.join(app.static_folder, "css")
        # normalize and join safely
        full = os.path.normpath(os.path.join(css_dir, filename))
        try:
            common = os.path.commonpath([css_dir, full])
        except Exception:
            return Response("/* forbidden */", mimetype="text/css", status=403)
        if common != os.path.normpath(css_dir):
            return Response("/* forbidden */", mimetype="text/css", status=403)
        if not os.path.exists(full):
            return Response("/* not found */", mimetype="text/css", status=404)
        with open(full, "r", encoding="utf-8") as f:
            css = f.read()
        # remove comments
        css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        # collapse whitespace
        css = re.sub(r"\s+", " ", css)
        # remove space around symbols
        css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
        # trim
        css = css.strip()
        resp = Response(css, mimetype="text/css")
        # cache in browser for 1 hour
        resp.headers["Cache-Control"] = "public, max-age=3600"
        return resp
    except Exception:
        return Response("/* error */", mimetype="text/css", status=500)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        try:
            ensure_project_file_column()
        except Exception:
            pass
    app.run(debug=True)
