from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c0d7bf0377e75f40c2431a3e5d9083a2'

posts = [
    {
        'author' : 'Michael Garrigan',
        'title' : 'First Blog Post',
        'content' : 'First post content',
        'date_posted' : 'Nov. 1, 2021'

    },
    {
        'author' : "J.R.R. Tolkien",
        'title' : "The Flight of the Noldor",
        'content' : "Yeah we fucked up.",
        'date_posted' : "YT 1106"

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)