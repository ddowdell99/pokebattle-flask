from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash

from app.auth.forms import UserCreation, UserLogin
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

            flash('Successfully created user!', 'success')

            return redirect(url_for('auth.logMeIn'))

    return render_template('signup.html', signUpForm=signUpForm)

@auth.route('/login', methods=['GET', 'POST'])
def logMeIn():
    
    logInForm = UserLogin()
    if request.method == 'POST':
        if logInForm.validate():
            username = logInForm.username.data
            password = logInForm.password.data

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash('Successfully logged in!', 'success')
                    login_user(user)
                    return redirect(url_for('homePage'))

                else:
                    flash('Incorrect Password!', 'danger')
            else:
                flash('User does not exist!', 'danger')


    return render_template('login.html', logInForm=logInForm)

@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))