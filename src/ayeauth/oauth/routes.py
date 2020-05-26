from flask import Blueprint, abort, render_template, request
from flask_login import current_user, login_required

from ayeauth.models.application import Application
from ayeauth.oauth.forms import AllowApplicationForm

oauth_bp = Blueprint(
    "oauth_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="assets",
)


@oauth_bp.route("/authorize", methods=["GET", "POST"])
@login_required
def authorize():
    response_type = request.args.get("response_type")
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    scopes = request.args.get("scope")
    state = request.args.get("state")

    form = AllowApplicationForm()

    if form.validate_on_submit():
        pass

    if response_type != "code":
        abort(400)

    application = Application.query.filter_by(client_id=client_id).first()
    if application is None:
        abort(400)
    if application.redirect_uri != redirect_uri:
        abort(400)

    scopes = [scope for scope in scopes.split(",") if scope != ""]
    for application_scope in application.scopes:
        if application_scope.scope.name not in scopes:
            abort(400)

    return render_template(
        "authorize.html",
        application=application,
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scopes=scopes,
        state=state,
        form=form,
        user=current_user,
    )


@oauth_bp.route("/token", methods=["POST"])
def token():
    pass
