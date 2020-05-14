from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, validators, SelectField, FieldList, FormField, TextAreaField

from ayeauth import _get_uuid
from ayeauth.models.application import Application
from ayeauth.models.scope import ScopeAccess, Scope


def generate_scope_select_fields():
    scopes = Scope.query.all()
    scope_field_list = []

    for scope in scopes:
        scope_field = ScopeSelectField()
        scope_field.id = _get_uuid()
        scope_field.scope.label = scope.name
        scope_field.scope.description = scope.description
        scope_field.scope.choices = [scope_access.value for scope_access in ScopeAccess]
        scope_field_list.append(scope_field)

    return scope_field_list


class ScopeSelectField(FlaskForm):
    scope = SelectField("", choices=[])


class ApplicationForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    description = TextAreaField("Description")
    callback_url = StringField("Callback URL", [validators.InputRequired()])
    scope_list = FieldList(FormField(ScopeSelectField))
    submit = SubmitField("Register Application")

    def validate(self):
        return False
