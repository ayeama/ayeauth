from flask_wtf import FlaskForm
from wtforms import SubmitField


class AllowApplicationForm(FlaskForm):
    allow = SubmitField("Allow")

    def validate(self):
        return True
