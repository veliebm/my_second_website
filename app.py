# Import the Flask class from the flask module.
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

# Create the application object.
app = Flask(__name__)

# config
app.secret_key = "be kind"
app.database = "sample.db"


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("login"))
    return wrap


# Use decorators to link the function to a url.
@app.route("/")
@login_required
def home():
    posts = []
    try:
        g.db = connect_db()
        cur = g.db.execute("select * from posts")

        for row in cur.fetchall():
            posts.append(dict(title=row[0], description=row[1]))

        g.db.close()
    except sqlite3.OperationalError:
        flash("You have no database!")

    return render_template("index.html", posts=posts)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")  # Render a template.


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid Credentials. Please try again."
        else:
            session["logged_in"] = True
            flash("You were just logged in!")
            return redirect(url_for("home"))
    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash("You were just logged out!")
    return redirect(url_for("welcome"))


def connect_db():
    return sqlite3.connect(app.database)


# Start the server with the "run()" method.
if __name__ == "__main__":
    app.run(debug=True)
