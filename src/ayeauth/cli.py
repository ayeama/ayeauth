import click

import ayeauth


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


@database.command("create")
@click.pass_context
def database_create(context):
    with context.obj.app_context():
        ayeauth.db.create_all()
        ayeauth.se.datastore.create_user(username="ayeama", password="password")
        ayeauth.db.session.commit()


if __name__ == "__main__":
    main()
