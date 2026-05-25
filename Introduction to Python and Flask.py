# app.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return "<h1>Welcome to My Flask App!</h1><p>This is the home page.</p>"

# Route for the about page
@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This page tells you about the app.</p>"

# Route for the contact page
@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1><p>You can contact us at: example@email.com</p>"

# Route for a custom page
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to the personalized page.</p>"

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
