from flask import Flask, render_template, redirect, url_for, request, flash
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
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# دیتابیس SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# مدیریت لاگین
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Babel برای چند زبانه بودن
app.config["LANGUAGES"] = ["en", "fa"]


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


# مدل کاربر
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


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


@app.route("/projects")
def projects():
    [
        {
            "title": "Flask Login Form",
            "desc": "A simple and secure login and registration system built using Python Flask with SQLite for data storage.",
            "tech": "Python, Flask, SQLite, html",
        },
        {
            "title": "Reservation System",
            "desc": "Online booking platform with appointment management for clients and admins.",
            "tech": "PHP, HTML, TailwindCSS",
        },
        {
            "title": "TeamVerse",
            "desc": " A collaborative gaming platform connecting players and teams for tournaments and group challenges.",
            "tech": "PHP, TailwindCSS",
        },
        {
            "title": "E-Commerce Platform",
            "desc": "Custom online store with full payment integration.",
            "tech": "Python, Flask, React.js, TailwindCSS",
        },
        {
            "title": "AI-Powered Dashboard",
            "desc": "Business analytics dashboard with real-time insights.",
            "tech": "Python, Flask, React.js, Chart.js",
        },
        {
            "title": "Portfolio Website",
            "desc": "Elegant personal site for professionals.",
            "tech": "Python, Flask, TailwindCSS",
        },
        {
            "title": "Inventory Management System",
            "desc": "Full-stack solution for tracking products and orders.",
            "tech": "Python, Flask, React.js, PostgreSQL",
        },
        {
            "title": "Social Media Platform",
            "desc": "Scalable web app for sharing content and connecting users.",
            "tech": "Python, Flask, React.js, Socket.IO",
        },
        {
            "title": "Task Automation App",
            "desc": "Automates repetitive business tasks for efficiency.",
            "tech": "Python, Flask, Celery, Redis",
        },
        {
            "title": "Company CRM System",
            "desc": "Customer relationship management for enterprise clients.",
            "tech": "Python, Flask, React.js, SQLAlchemy",
        },
        {
            "title": "Blog & CMS Platform",
            "desc": "Dynamic content management system for blogs and articles.",
            "tech": "Python, Flask, React.js, TailwindCSS",
        },
        {
            "title": "Event Booking Platform",
            "desc": "Complete system for booking events and ticket management.",
            "tech": "Python, Flask, React.js, Stripe API",
        },
        {
            "title": "Online Learning Platform",
            "desc": "E-learning solution with courses, quizzes, and certificates.",
            "tech": "Python, Flask, React.js, PostgreSQL",
        },
        {
            "title": "Project Management Tool",
            "desc": "Organize teams, tasks, and timelines efficiently.",
            "tech": "Python, Flask, React.js, TailwindCSS",
        },
        {
            "title": "IoT Device Dashboard",
            "desc": "Monitor and manage IoT devices remotely.",
            "tech": "Python, Flask, React.js, MQTT",
        },
        {
            "title": "Real Estate Listing Platform",
            "desc": "Property management and listing platform for agents.",
            "tech": "Python, Flask, React.js, PostgreSQL",
        },
        {
            "title": "Healthcare Management System",
            "desc": "Manage patients, appointments, and medical records.",
            "tech": "Python, Flask, React.js, SQLAlchemy",
        },
        {
            "title": "FinTech Payment App",
            "desc": "Secure financial transactions and account management.",
            "tech": "Python, Flask, React.js, Stripe API",
        },
    ]
    return render_template("projects.html", projects=projects_list)


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ثبت‌نام
@app.route("/register", methods=["GET", "POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    if User.query.filter_by(username=username).first():
        flash(_("Username already exists!"), "danger")
        return redirect(url_for("login"))
    if User.query.filter_by(email=email).first():
        flash(_("Email already exists!"), "danger")
        return redirect(url_for("login"))

    new_user = User(username=username, email=email)
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
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
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


# خروج
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

with app.app_context():
    db.create_all()  # مطمئن شو جدول‌ها ساخته شدن
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", email="admin@example.com")
        admin.set_password("123456")  # رمز ورود دلخواه
        db.session.add(admin)
        db.session.commit()




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
