from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, validators

from ayeauth.auth.password import verify_password
from ayeauth.models.user import User


class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    confirm = PasswordField(
        "Confirm password", [validators.InputRequired(), validators.EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate(self):
        if not super(RegisterForm, self).validate():
            return False

        user = User.query.filter_by(username=self.username.data).first()

        if user is not None:
            return False

        return True


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        self.user = User.query.filter_by(username=self.username.data).first()

        if self.user is None:
            return False
        if not self.user.is_active:
            return False
        if not verify_password(self.password.data, self.user.password):
            return False

        return True
