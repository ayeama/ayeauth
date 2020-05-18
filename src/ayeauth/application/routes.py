from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

from ayeauth import db
from ayeauth.application.forms import ApplicationForm
from ayeauth.models.application import Application

application_bp = Blueprint(
    "application_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@application_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = ApplicationForm()

    if form.validate_on_submit():
        application = Application(
            form.name.data, form.description.data, form.callback_url.data
        )
        db.session.add(application)
        db.session.commit()

        return redirect(url_for("home_bp.index"))

    return render_template("create.html", form=form, user=current_user)
