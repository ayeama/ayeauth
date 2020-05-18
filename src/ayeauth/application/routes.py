from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

from ayeauth import db
from ayeauth.application.forms import ApplicationForm
from ayeauth.models.application import Application
from ayeauth.models.application_scope import ApplicationScope
from ayeauth.models.scope import Scope, ScopeAccess

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
        application_scope = ApplicationScope(scope_access=ScopeAccess.NO_ACCESS)
        application_scope.scope = Scope.query.filter_by(name="Username").first()
        application.scopes.append(application_scope)

        db.session.add(application)
        db.session.commit()

        return redirect(url_for("home_bp.index"))

    return render_template("create.html", form=form, user=current_user)
