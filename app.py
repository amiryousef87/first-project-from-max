from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    lang = request.args.get("lang")
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.context_processor
def inject_direction():
    lang = get_locale()
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

if __name__ == "__main__":
    app.run(debug=True)
