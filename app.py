# Import the Flask class from the flask module.
from flask import Flask, render_template

# Create the application object.
app = Flask(__name__)

# Use decorators to link the function to a url.
@app.route("/")
def home():
    return "Hello, World!"  # Return a string.

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")  # Render a template.

# Start the server with the "run()" method.
if __name__ == "__main__":
    app.run(debug=True)
