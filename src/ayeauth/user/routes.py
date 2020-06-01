from flask import Blueprint, abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required

from ayeauth.user.forms import ChangePasswordForm
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


@user_bp.route("/settings", methods=["GET", "POST"])
@user_bp.route("/settings/<setting>", methods=["GET", "POST"])
@login_required
def settings(setting=SETTING_LIST[0]):
    template_kwargs = {}
    setting = setting.lower()
    if setting not in SETTING_LIST:
        abort(404)

    template_kwargs["settings"] = SETTING_LIST
    template_kwargs["selected_setting"] = setting

    if setting == "profile":
        change_password_form = ChangePasswordForm()
        if change_password_form.validate_on_submit():
            current_user.set_password(change_password_form.new_password.data)
            flash("Successfully changed password", "success")
            return redirect(url_for("user_bp.settings", setting="profile"))
        if request.method == "POST":
            flash("Failure to change password. Make sure you have entered your current password and that the new passwords match", "danger")
        template_kwargs["change_password_form"] = change_password_form

    return render_template("settings.html", user=current_user, **template_kwargs)
