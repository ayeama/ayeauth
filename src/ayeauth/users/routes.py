from flask import Blueprint, render_template
from flask_login import current_user

users_bp = Blueprint(
    "users_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@users_bp.route("/")
def index():
    return render_template("layout.html", user=current_user)


@users_bp.route("/<username>")
def profile(username):
    return {"hello": username}, 200
