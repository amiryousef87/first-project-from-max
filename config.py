import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-prod")
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fa"]
