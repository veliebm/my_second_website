###############
### Imports ###
###############

from project import app, db
from project.models import BlogPost
from flask import render_template, redirect, url_for, session, flash, Blueprint
from functools import wraps

##############
### Config ###
##############

home_blueprint = Blueprint("home", __name__, template_folder="templates")

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


@home_blueprint.route("/")
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@home_blueprint.route("/welcome")
def welcome():
    return render_template("welcome.html")
