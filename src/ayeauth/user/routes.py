from flask import Blueprint, abort, render_template
from flask_login import current_user, login_required

from ayeauth.models.user import User

user_bp = Blueprint(
    "user_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)

SETTING_LIST = ["profile", "applications"]


@user_bp.route("/<username>")
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    return render_template("profile.html", user=current_user, profile_user=user)


@user_bp.route("/settings")
@user_bp.route("/settings/<setting>")
@login_required
def settings(setting=SETTING_LIST[0]):
    template_kwargs = {}
    setting = setting.lower()
    if setting not in SETTING_LIST:
        abort(404)

    template_kwargs["settings"] = SETTING_LIST
    template_kwargs["selected_setting"] = setting

    return render_template("settings.html", user=current_user, **template_kwargs)
