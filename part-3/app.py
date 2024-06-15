#importing the Flask Class from flask library
from flask import Flask ,render_template

#making an object of the flask class
my_app= Flask(__name__)

#creating an endpoint
@my_app.route("/")
@my_app.route("/home") #for same function we can have multiple nodes
def home_page():
    return render_template("home.html")

#creating another endpoint
@my_app.route("/about")
def about_page():
    return render_template("about.html")

#one way to run the flask app
if __name__=="__main__":
    my_app.run(debug=True)