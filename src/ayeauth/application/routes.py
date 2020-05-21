from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from wtforms import SelectField

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


def _generate_scope_fields():
    for scope in Scope.query.all():
        setattr(
            ApplicationForm,
            f"scope_{scope.name.lower()}",
            SelectField(
                scope.name,
                description=scope.description,
                choices=[x.value for x in ScopeAccess],
            ),
        )


@application_bp.route("/test")
def test():
    sa = Scope("Username", "View your username")
    sb = Scope("Scopes", "View your scopes")
    db.session.add(sa)
    db.session.add(sb)
    db.session.commit()
    return redirect(url_for("home_bp.index"))


@application_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    _generate_scope_fields()
    form = ApplicationForm()

    if form.validate_on_submit():
        application = Application(
            form.name.data, form.description.data, form.callback_url.data
        )
        db.session.add(application)
        for scope in [x for x in form if x.id.startswith("scope_")]:
            application_scope = ApplicationScope(scope_access=ScopeAccess(scope.data))
            application_scope.scope = Scope.query.filter_by(
                name=scope.name[6:].capitalize()
            ).first()
            application.scopes.append(application_scope)

        db.session.commit()

        return redirect(url_for("home_bp.index"))

    return render_template("create.html", form=form, user=current_user)
