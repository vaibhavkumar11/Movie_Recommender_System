from flask import render_template,url_for, flash, redirect, session
import numpy as np
from movie.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from movie import app, mongo, bcrypt


@app.route("/")
@app.route('/home')
def home():
    movies = mongo.db.movies.find()
    return render_template('home.html', title='Home', movies=movies[:20])

@app.route("/about")
def about():
    return render_template('rate.html')

@app.route('/pred')
def pred():
    return render_template('pred.html')

@app.route('/register', methods=['GET',  'POST'])
def register():
    form = RegistrationForm()
    users = mongo.db.users
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        users.insert({'username':form.username.data, 'email':form.email.data, 'password':hashed_password})
        session['username'] = form.username.data
        flash(f'Account created for {form.username.data}!You will be able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title="Login", form=form)