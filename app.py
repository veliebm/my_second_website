# Import the Flask class from the flask module.
from flask import Flask, render_template, redirect, url_for, request

# Create the application object.
app = Flask(__name__)

# Use decorators to link the function to a url.
@app.route("/")
def home():
    return "Hello, World!"  # Return a string.

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
            return redirect(url_for("home"))
    return render_template("login.html", error=error)

# Start the server with the "run()" method.
if __name__ == "__main__":
    app.run(debug=True)
