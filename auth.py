from flask import session, flash, redirect, url_for
from werkzeug.security import check_password_hash
from functools import wraps
from models import User


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

def login_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first!', 'warning')
            return redirect(url_for('app.login'))
        return f(*args, **kwargs)
    return decorated_func