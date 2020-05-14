from flask import Blueprint, render_template
from flask_login import current_user, login_required

from ayeauth.application.forms import ApplicationForm, generate_scope_select_fields

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
    form.scope_list = generate_scope_select_fields()

    if form.validate_on_submit():
        pass

    return render_template("create.html", form=form, user=current_user)


@application_bp.route("/test")
def test():
    from ayeauth import db
    from ayeauth.models.scope import Scope

    a = Scope("email", "")
    b = Scope("username", "")
    c = Scope("dateofbirth", "")
    db.session.add(a)
    db.session.add(b)
    db.session.add(c)
    db.session.commit()

    return {}
