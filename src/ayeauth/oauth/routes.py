from datetime import datetime, timedelta

from flask import (
    Blueprint,
    abort,
    current_app,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required

from ayeauth import db
from ayeauth.models.application import Application
from ayeauth.models.authorization_code import AuthorizationCode
from ayeauth.oauth.forms import AllowApplicationForm
from ayeauth.oauth.token import encode_jwt

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

    application = Application.query.filter_by(client_id=client_id).first()
    form = AllowApplicationForm()

    if response_type != "code":
        abort(400)

    if application is None:
        abort(400)
    if application.redirect_uri != redirect_uri:
        abort(400)

    _scopes = scopes
    scopes = [scope for scope in scopes.split(" ") if scope != ""]
    for application_scope in application.scopes:
        # NOTE: this only checks one way. Is it needed?
        if application_scope.scope.name not in scopes:
            abort(400)

    if (
        current_user.is_authenticated
        and application in current_user.authorized_applications
    ):
        return redirect(url_for("home_bp.index"))

    if form.validate_on_submit():
        current_user.authorized_applications.append(application)
        db.session.commit()
        # TODO: check for existing vaild auth code first and abort if one exists?
        auth_code = AuthorizationCode(
            datetime.utcnow()
            + timedelta(seconds=current_app.config["AUTHORIZATION_CODE_EXPIRY"]),
            current_user.id,
            application.id,
        )
        db.session.add(auth_code)
        db.session.commit()
        return redirect(
            f"{application.redirect_uri}?code={auth_code.code}&state={state}"
        )

    return render_template(
        "authorize.html",
        application=application,
        response_type=response_type,
        client_id=client_id,
        redirect_uri=redirect_uri,
        scopes=_scopes,
        state=state,
        form=form,
        user=current_user,
    )


@oauth_bp.route("/token", methods=["POST"])
def token():
    grant_type = request.args["grant_type"]
    code = request.args["code"]
    redirect_uri = request.args["redirect_uri"]
    client_id = request.args["client_id"]
    # client_secret = request.args["client_secret"]

    if grant_type != "authorization_code":
        abort(400)

    auth_code = AuthorizationCode.query.filter_by(code=code).first()
    if auth_code is None or auth_code.expiry < datetime.utcnow():
        abort(400)

    application = Application.query.filter_by(client_id=client_id).first()
    if application is None or application.redirect_uri != redirect_uri:
        abort(400)

    access_token = encode_jwt(auth_code.user_id, application.client_id).decode()
    return (
        {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": current_app.config["JWT_EXPIRATION"],
            "state": auth_code.state,
        },
        200,
    )


@oauth_bp.route("/userinfo")
def userinfo():
    pass
