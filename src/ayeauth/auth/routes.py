from flask import Blueprint, current_app, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from flask_principal import Identity, identity_changed

from ayeauth.auth.forms import LoginForm

auth_bp = Blueprint(
    "auth_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    return render_template("/auth/register.html", user=current_user)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)
        identity_changed.send(
            current_app._get_current_object(), identity=Identity(form.user.id)
        )
        return redirect(url_for("users_bp.index"))

    return render_template("/auth/login.html", form=form, user=current_user)


@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))
