from flask import render_template,url_for, flash, redirect, session, request
from movie.forms import RegistrationForm, LoginForm
from movie import app, db, bcrypt, mongo
from movie.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route('/home')
def home():
    movies = mongo.db.movies.find()
    return render_template('home.html', title='Home', movies=movies[:20])

@app.route("/about")
def about():
    return render_template('rate.html')

@app.route('/register', methods=['GET',  'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/rate')
@login_required
def rate():
    return render_template('rate.html', title='Rate-Movies')
