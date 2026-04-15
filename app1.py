from flask import Flask,redirect

app=Flask(__name__)

@app.route("/admin")
def admin():
    return "welcome to admin page"

@app.route("/user/<username>")
def user(username):
    if username=="admin":
        return redirect("/admin")
    else:
        return f"welcome to {username}'s page"
    
app.run(debug=True)