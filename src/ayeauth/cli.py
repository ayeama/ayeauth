import click

import ayeauth
from ayeauth.auth.password import hash_password
from ayeauth.models.role import Role
from ayeauth.models.user import User


@click.group()
@click.pass_context
def main(context):
    context.obj = ayeauth.create()


@main.command("run")
@click.option("--debug", is_flag=True)
@click.pass_context
def run(context, debug):
    context.obj.run(debug=debug)


@main.group("database")
@click.pass_context
def database(context):
    pass


@database.command("initialize")
@click.pass_context
def database_initialize(context):
    with context.obj.app_context():
        ayeauth.db.create_all()
        ayeauth.db.session.commit()


@database.command("delete")
@click.pass_context
def database_delete(context):
    with context.obj.app_context():
        ayeauth.db.drop_all()
        ayeauth.db.session.commit()


@database.group("model")
@click.pass_context
def database_model(context):
    pass


@database_model.group("Role")
@click.pass_context
def model_role(context):
    pass


@model_role.command("get")
@click.option("--many", "-m", is_flag=True)
@click.option("--id", "-i")
@click.pass_context
def model_role_get(context, many, id):
    with context.obj.app_context():
        if many:
            role = Role.query.all()
        else:
            role = Role.query.filter_by(id=id).first()
        click.echo(repr(role))


@model_role.command("post")
@click.option("--name", "-n", required=True)
@click.option("--description", "-d")
@click.pass_context
def model_role_post(context, name, description):
    with context.obj.app_context():
        role = Role(name, description)
        ayeauth.db.session.add(role)
        ayeauth.db.session.commit()
        click.echo(repr(role))


@model_role.command("put")
@click.option("--id", "-i", required=True)
@click.option("--name", "-n")
@click.option("--description", "-d")
@click.pass_context
def model_role_put(context, id, name, description):
    with context.obj.app_context():
        role = Role.query.filter_by(id=id).first()
        if name:
            role.name = name
        if description:
            role.description = description
        ayeauth.db.session.commit()
        click.echo(repr(role))


@model_role.command("delete")
@click.option("--id", "-i", required=True)
@click.pass_context
def model_role_delete(context, id):
    with context.obj.app_context():
        role = Role.query.filter_by(id=id).first()
        ayeauth.db.session.delete(role)
        ayeauth.db.session.commit()


@database_model.group("User")
@click.pass_context
def model_user(context):
    pass


@model_user.command("get")
@click.option("--many", "-a", is_flag=True)
@click.option("--id", "-i")
@click.pass_context
def model_user_get(context, many, id):
    with context.obj.app_context():
        if many:
            user = User.query.all()
        else:
            user = User.query.filter_by(id=id).first()
        click.echo(repr(user))


@model_user.command("post")
@click.option("--username", "-u", required=True)
@click.option("--password", "-p", required=True)
@click.pass_context
def model_user_post(context, username, password):
    with context.obj.app_context():
        user = User(username, password)
        ayeauth.db.session.add(user)
        ayeauth.db.session.commit()
        click.echo(repr(user))


@model_user.command("put")
@click.option("--id", "-i", required=True)
@click.option("--username", "-u")
@click.option("--password", "-p")
@click.pass_context
def model_user_put(context, id, username, password):
    with context.obj.app_context():
        user = User.query.filter_by(id=id).first()
        if username:
            user.username = username
        if password:
            user.password = hash_password(password)
        ayeauth.db.session.commit()
        click.echo(repr(user))


@model_user.command("delete")
@click.option("--id", "-i", required=True)
@click.pass_context
def model_user_delete(context, id):
    with context.obj.app_context():
        user = User.query.filter_by(id=id).first()
        ayeauth.db.session.delete(user)
        ayeauth.db.session.commit()


if __name__ == "__main__":
    main()
