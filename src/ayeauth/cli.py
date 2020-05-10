import click

import ayeauth
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
        ayeauth.se.datastore.create_user(username="ayeama", password="password")
        ayeauth.db.session.commit()


@database.group("model")
@click.pass_context
def database_model(context):
    pass


@database_model.group("User")
@click.pass_context
def model_user(context):
    pass


@model_user.command("get")
@click.option("--all", "-a", "_all", is_flag=True)
@click.option("--username", "-u")
@click.pass_context
def model_user_get(context, _all, username):
    with context.obj.app_context():
        if _all:
            click.echo(User.query.all())
        click.echo(User.query.filter_by(username=username).first())


@model_user.command("post")
@click.option("--username", "-u", required=True, type=str)
@click.option("--password", "-p", required=True, type=str)
@click.option("--role", "-r", multiple=True, type=str)
@click.pass_context
def model_user_post(context, username, password, role):
    with context.obj.app_context():
        ayeauth.se.datastore.create_user(username=username, password=password)
        ayeauth.db.session.commit()


if __name__ == "__main__":
    main()
