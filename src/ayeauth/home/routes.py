from flask import Blueprint, render_template
from flask_login import current_user

home_bp = Blueprint(
    "home_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@home_bp.route("/")
def index():
    return render_template("index.html", user=current_user)


def error_page(e):
    return render_template("error.html", error=e, user=current_user), e.code
