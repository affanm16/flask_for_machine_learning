#importing the Flask Class from flask library
from flask import Flask ,render_template,url_for

from employees import employees_data

#making an object of the flask class
my_app= Flask(__name__)

#creating an endpoint
@my_app.route("/")
@my_app.route("/home") #for same function we can have multiple nodes
def home_page():
    return render_template(
        "home.html",
        title="Home")  #title is parameter

#creating another endpoint
@my_app.route("/about")
def about_page():
    return render_template("about.html",title="About")

@my_app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template(
        "evaluate.html",
        title="Evaluate",
        number=num
    )

@my_app.route("/employees")
def employees():
    return render_template(
        "employees.html",
        emps="employees_data"
    )

#one way to run the flask app
if __name__=="__main__":
    my_app.run(debug=True)