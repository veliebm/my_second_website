###############
### Imports ###
###############

from project import app, db
from project.models import BlogPost
from flask import render_template, Blueprint
from flask.ext.login import login_required

##############
### Config ###
##############

home_blueprint = Blueprint("home", __name__, template_folder="templates")

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
