###############
### Imports ###
###############

from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import os

##############
### Config ###
##############

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# Register our blueprints.
app.register_blueprint(users_blueprint)

########################
### Helper functions ###
########################


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for("users.login"))
    return wrap


##############
### Routes ###
##############


@app.route("/")
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


##################
### Run server ###
##################

if __name__ == "__main__":
    app.run()
