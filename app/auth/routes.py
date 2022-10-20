from flask import Blueprint, render_template, request, redirect, url_for
# from flask_login import login_user, logout_user, current_user
# from .forms import LoginForm, UserCreationForm
# from app.models import User
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signMeUp():
    return render_template('signup.html')

@auth.route('/login', methods=['GET', 'POST'])
def logMeIn():
    return render_template('login.html')