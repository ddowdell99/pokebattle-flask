from flask import Blueprint, render_template, request, redirect, url_for
# from flask_login import login_user, logout_user, current_user
# from .forms import LoginForm, UserCreationForm
from werkzeug.security import check_password_hash

from app.auth.forms import UserCreation
from app.models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signMeUp():
    signUpForm = UserCreation()

    if request.method == 'POST':
        if signUpForm.validate():
            first_name = signUpForm.first_name.data
            last_name = signUpForm.last_name.data
            username = signUpForm.username.data
            email = signUpForm.email_address.data
            password = signUpForm.password.data

            user = User(first_name, last_name, username, email, password)

            user.saveToDB()

            return redirect(url_for('auth.logMeIn'))

    return render_template('signup.html', signUpForm=signUpForm)

@auth.route('/login', methods=['GET', 'POST'])
def logMeIn():
    return render_template('login.html')