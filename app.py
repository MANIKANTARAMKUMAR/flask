from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    return "hello world"


@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return f"sum of {a} and {b} is  {a+b}"

@app.route("/sub/<int:a>/<int:b>")
def sub(a,b):
    return f"sub of {a} and {b} is {a-b}"
app.run(debug=True)