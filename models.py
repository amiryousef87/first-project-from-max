from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

#  جدول نشست های فعال


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    device = db.Column(db.String(120))
    browser = db.Column(db.String(120))
    last_active = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50))
    is_current = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Session {self.device} - {self.browser}>"


# جدول کاربران

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# جدول داده‌های داشبورد


class DashboardData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(100))
    value = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship(
        'User', backref=db.backref('dashboard_data', lazy=True))


# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     desc = db.Column(db.Text, nullable=False)
#     tech = db.Column(db.String(200), nullable=False)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    tech = db.Column(db.String(300), nullable=True)
    project_file = db.Column(db.String(300), nullable=True)


class Product(db.Model):
    __tablename__ = 'products'  # نکته مهم! جمعش کن تا با تداخل نداشته باشه

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
