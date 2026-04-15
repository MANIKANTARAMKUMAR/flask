from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def index():
    return "welcome to the home page"

@app.route("/admin")
def admin():
    return "welcome to admin page"

@app.route("/user/<username>")
def user(username):
    if username=="admin":
        return redirect(url_for("admin"))
    else:
        return f"welcome to {username}'s page"
app.run(debug=True)