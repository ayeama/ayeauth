from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators

from ayeauth.models.application import Application


class ApplicationForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    description = TextAreaField("Description")
    redirect_uri = StringField("Redirect URI", [validators.InputRequired()])
    submit = SubmitField("Register Application")

    def validate(self):
        application = Application.query.filter_by(name=self.name.data).first()

        if application is not None:
            return False

        return True
