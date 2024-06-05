#importing the Flask Class from flask library
from flask import Flask

#making an object of the flask class
my_app= Flask(__name__)

#creating an endpoint
@my_app.route("/")
def home_page():
    return "<h1> Welcome to the Home Page!</h1>" #h1-html's header tag

#creating another endpoint
@my_app.route("/about")
def about_page():
    return "<h1> Welcome to the About Page!</h1>" #h1-html's header tag


#one way to run the flask app
if __name__=="__main__":
    my_app.run(debug=True)