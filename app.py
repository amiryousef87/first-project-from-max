from flask import Flask, render_template, request, jsonify
from flask_babel import Babel, gettext as _
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# تابع انتخاب زبان
def select_locale():
    lang = request.args.get("lang")
    if lang and lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])

# حالا babel را با این تابع مقداردهی کن
babel = Babel(app, locale_selector=select_locale)

@app.context_processor
def inject_direction():
    lang = select_locale()
    return {
        "current_lang": lang,
        "dir": "rtl" if lang == "fa" else "ltr"
    }

@app.route("/")
def index():
    return render_template("index.html", title=_("Home"))

@app.route("/about")
def about():
    return render_template("about.html", title=_("About"))

@app.route("/projects")
def projects():
    projects_list = [
        {"title": "E-Commerce Platform", "desc": "Custom online store with full payment integration.", "tech": "Python, Flask, React.js, TailwindCSS"},
        {"title": "AI-Powered Dashboard", "desc": "Business analytics dashboard with real-time insights.", "tech": "Python, Flask, React.js, Chart.js"},
        {"title": "Portfolio Website", "desc": "Elegant personal site for professionals.", "tech": "Python, Flask, TailwindCSS"},
        {"title": "Inventory Management System", "desc": "Full-stack solution for tracking products and orders.", "tech": "Python, Flask, React.js, PostgreSQL"},
        {"title": "Social Media Platform", "desc": "Scalable web app for sharing content and connecting users.", "tech": "Python, Flask, React.js, Socket.IO"},
        {"title": "Task Automation App", "desc": "Automates repetitive business tasks for efficiency.", "tech": "Python, Flask, Celery, Redis"},
        {"title": "Company CRM System", "desc": "Customer relationship management for enterprise clients.", "tech": "Python, Flask, React.js, SQLAlchemy"},
        {"title": "Blog & CMS Platform", "desc": "Dynamic content management system for blogs and articles.", "tech": "Python, Flask, React.js, TailwindCSS"},
        {"title": "Event Booking Platform", "desc": "Complete system for booking events and ticket management.", "tech": "Python, Flask, React.js, Stripe API"},
        {"title": "Online Learning Platform", "desc": "E-learning solution with courses, quizzes, and certificates.", "tech": "Python, Flask, React.js, PostgreSQL"},
        {"title": "Project Management Tool", "desc": "Organize teams, tasks, and timelines efficiently.", "tech": "Python, Flask, React.js, TailwindCSS"},
        {"title": "IoT Device Dashboard", "desc": "Monitor and manage IoT devices remotely.", "tech": "Python, Flask, React.js, MQTT"},
        {"title": "Real Estate Listing Platform", "desc": "Property management and listing platform for agents.", "tech": "Python, Flask, React.js, PostgreSQL"},
        {"title": "Healthcare Management System", "desc": "Manage patients, appointments, and medical records.", "tech": "Python, Flask, React.js, SQLAlchemy"},
        {"title": "FinTech Payment App", "desc": "Secure financial transactions and account management.", "tech": "Python, Flask, React.js, Stripe API"},
    ]
    return render_template("projects.html", title="Projects", projects=projects_list)


@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/dashboard")
def dashboard():
    return render_template("dashborad.html", title="Dashboard")


@app.route('/add-project', methods=['POST'])
def add_project():
    title = request.form['title']
    desc = request.form['desc']
    tech = request.form['tech']
    # ذخیره در دیتابیس یا لیست
    new_project = {'title': title, 'desc': desc, 'tech': tech}
    return jsonify(new_project)



if __name__ == "__main__":
    app.run(debug=True)

