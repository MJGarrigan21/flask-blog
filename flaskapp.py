from flask import Flask, render_template
app = Flask(__name__)

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