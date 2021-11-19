from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post


posts = [
    {
        'author': 'Michael Garrigan',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': 'Nov. 1, 2021'

    },
    {
        'author': "J.R.R. Tolkien",
        'title': "The Flight of the Noldor",
        'content': "Yeah we fucked up.",
        'date_posted': "YT 1106"

    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccsesful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
