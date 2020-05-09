from flask import Blueprint

users_bp = Blueprint(
    'users_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)


@users_bp.route('/')
def index():
    return {"hello": "world"}, 200


@users_bp.route('/<username>')
def profile(username):
    return {"hello": username}, 200


@users_bp.route('/create')
def create():
    from ayeauth import db

    db.create_all()
    # user_datastore.create_user(email='a@a.com', password='password')
    db.session.commit()

    return {"hello": "world"}, 200
