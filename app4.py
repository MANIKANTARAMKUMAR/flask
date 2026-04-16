from flask import Flask,redirect,url_for
app=Flask(__name__)

#string converter
@app.route("/course/<coursename>")
def course(coursename):
    print(type(coursename))
    return f"welcome to {coursename} course"

#int converter
@app.route("/course/<int:courseid>")
def courseid(courseid):
    print(type(courseid))
    return f"half of course id is {courseid/2}"


#float converter
@app.route("/course/<float:courseprice>")
def courseprice(courseprice):
    print(type(courseprice))
    return f"welcome to course with price {courseprice*2}"

#path converter
@app.route("/course/<path:filename>")    
def showfile(filename):
    print(type(filename))
    return f"welcome to course with filename {filename}"

#uuid converter

@app.route("/course/<uuid:courseid>")
def courseuuid(courseid):
    print(type(courseid))
    return f"welcome to course with uuid {courseid}"


app.run(debug=True)