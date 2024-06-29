from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    flash
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
@app.route("/signup" , methods=["GET", "POST"])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        flash(f"{form.username.data} Successfully Registered")
        return redirect(url_for("home"))
    
    return render_template("signup.html",title="SIGN UP",form=form)

#end point for login
@app.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm()
    email=form.email.data
    pw=form.password.data
    if form.validate_on_submit():
        if email=="abc@gmail.com" and pw=="12345678":
            flash("Logged in Successfully")
            return redirect(url_for("home"))
        else:
          flash("Incorrect Email or Password")  
    return render_template("login.html",title="LOGIN",form=form)

if __name__=="__main__":
    app.run(debug=True)