from flask_wtf import FlaskForm
from wtforms import (
    FieldList,
    FormField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
)

from ayeauth.models import _get_uuid
from ayeauth.models.scope import Scope, ScopeAccess


def scope_select_fields():
    l = []
    for scope in Scope.query.all():
        ssf = ScopeSelectField()
        ssf.id = _get_uuid()
        ssf.scope.label = scope.name
        ssf.scope.description = scope.description
        ssf.scope.choices = [scope_access.value for scope_access in ScopeAccess]
        l.append(ssf)

    return l


class ScopeSelectField(FlaskForm):
    scope = SelectField("", choices=[])


class ApplicationForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    description = TextAreaField("Description")
    callback_url = StringField("Callback URL", [validators.InputRequired()])
    scope_select_fields = FieldList(FormField(ScopeSelectField))
    submit = SubmitField("Register Application")

    def validate(self):
        return False
