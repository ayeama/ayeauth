from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
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
    return render_template("/auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        login_user(form.user, form.remember.data)
        identity_changed.send(
            current_app._get_current_object(), identity=Identity(form.user)
        )
        redirect("/")

    return render_template("/auth/login.html", form=form)


@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    redirect(url_for("auth_bp.login"))
