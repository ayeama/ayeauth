import click

import ayeauth
from ayeauth.models.role import RoleDatastore
from ayeauth.models.user import UserDatastore


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


@database.group("model")
@click.pass_context
def database_model(context):
    pass


@database_model.group("Role")
@click.pass_context
def model_role(context):
    pass


@model_role.command("get")
@click.option("--all", "-a", "_all", is_flag=True)
@click.option("--id", "-i")
@click.pass_context
def model_role_get(context, _all, id):
    with context.obj.app_context():
        click.echo(repr(RoleDatastore().get(id, many=_all)))


@model_role.command("post")
@click.option("--name", "-n", required=True)
@click.option("--description", "-d")
@click.pass_context
def model_role_post(context, name, description):
    with context.obj.app_context():
        click.echo(repr(RoleDatastore().post(name, description)))


@model_role.command("put")
@click.option("--id", "-i", required=True)
@click.option("--name", "-n")
@click.option("--description", "-d")
@click.pass_context
def model_role_put(context, id, name, description):
    with context.obj.app_context():
        click.echo(repr(RoleDatastore().put(id, name, description)))


@model_role.command("delete")
@click.option("--id", "-i", required=True)
@click.pass_context
def model_role_delete(context, id):
    with context.obj.app_context():
        click.echo(repr(RoleDatastore().delete(id)))


@database_model.group("User")
@click.pass_context
def model_user(context):
    pass


@model_user.command("add-role")
@click.option("--user-id", "-u", required=True)
@click.option("--role-id", "-r", required=True)
@click.pass_context
def model_user_add_role(context, user_id, role_id):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().add_role(user_id, role_id)))


@model_user.command("get-roles")
@click.option("--user-id", "-u", required=True)
@click.pass_context
def model_user_get_roles(context, user_id):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().get_roles(user_id)))


@model_user.command("delete-role")
@click.option("--user-id", "-u", required=True)
@click.option("--role-id", "-r", required=True)
@click.pass_context
def model_user_delete_role(context, user_id, role_id):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().delete_role(user_id, role_id)))


@model_user.command("get")
@click.option("--all", "-a", "_all", is_flag=True)
@click.option("--id", "-i")
@click.pass_context
def model_user_get(context, _all, id):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().get(id, many=_all)))


@model_user.command("post")
@click.option("--username", "-u", required=True)
@click.option("--password", "-p", required=True)
@click.pass_context
def model_user_post(context, username, password):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().post(username=username, password=password)))


@model_user.command("put")
@click.option("--id", "-i", required=True)
@click.option("--username", "-u")
@click.option("--password", "-p")
@click.pass_context
def model_user_put(context, id, username, password):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().put(id, username, password)))


@model_user.command("delete")
@click.option("--id", "-i", required=True)
@click.pass_context
def model_user_delete(context, id):
    with context.obj.app_context():
        click.echo(repr(UserDatastore().delete(id)))


if __name__ == "__main__":
    main()
