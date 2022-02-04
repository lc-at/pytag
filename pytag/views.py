from flask import Blueprint

bp = Blueprint('api', __name__)

@bp.route('/')
def home():
    return 'hello world'

