from flask import Blueprint, render_template
from flask_login import current_user

oauth_bp = Blueprint(
    "oauth_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@oauth_bp.route("/")
def index():
    return render_template("index.html", user=current_user)
