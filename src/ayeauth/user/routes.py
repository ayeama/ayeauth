from flask import Blueprint

user_bp = Blueprint(
    "user_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@user_bp.route("/profile")
def profile():
    pass


@user_bp.route("/settings")
def settings():
    pass
