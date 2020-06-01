from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators

from ayeauth.auth.password import verify_password


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Current password", [validators.InputRequired()])
    new_password = PasswordField("New password", [validators.InputRequired()])
    confirm_new_password = PasswordField(
        "Confirm new password",
        [validators.InputRequired(), validators.EqualTo("new_password")],
    )
    submit = SubmitField("Change password")

    def validate(self):
        if not super(ChangePasswordForm, self).validate():
            return False

        if not verify_password(self.current_password.data, current_user.password):
            return False

        return True
