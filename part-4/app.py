from flask import (
    Flask,
    render_template,
    url_for
    )
from forms import SignupForm,LoginForm
app =Flask(__name__)
#for csrf token
app.config["SECRET_KEY"]="24748"

#creating end points
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="HOME")

#end point for signup
@app.route("/signup")
def signup():
    form=SignupForm()
    return render_template("signup.html",title="SIGN UP",form=form)

#end point for login
@app.route("/login")
def login():
    form=LoginForm()
    return render_template("login.html",title="LOGIN",form=form
    )

if __name__=="__main__":
    app.run(debug=True)