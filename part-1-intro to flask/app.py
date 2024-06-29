#importing the Flask Class from flask library
from flask import Flask

#making an object of the flask class
my_app= Flask(__name__)

#creating an endpoint
@my_app.route("/")
@my_app.route("/home") #for same function we can have multiple nodes
def home_page():
    return "<h1> Welcome to the Home Page!</h1>" #h1-html's header tag

#creating another endpoint
@my_app.route("/about")
def about_page():
    return "<h1> Welcome to the About Page!</h1>" #h1-html's header tag

@my_app.route("/welcome/<name>")
def welcome_page(name):
    return f"<h1>Hi {name.title()},You are welcome to this page</h1>"
#title function capitalizes the name(i.e string)


@my_app.route("/addition/<int:num1>/<int:num2>")
def addition_two_nums(num1,num2):
    return f"<h1>Addition of {num1} and {num2} is {num2+num1}</h1>"

#one way to run the flask app
if __name__=="__main__":
    my_app.run(debug=True)