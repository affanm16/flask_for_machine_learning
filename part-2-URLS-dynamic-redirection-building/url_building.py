from flask import Flask , redirect, url_for
app= Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/pass/<sname><int:marks>")
def passed(sname,marks):
    return f"<h1>Congrats {sname.title()}, you have passed with {marks} marks!</h1>"

@app.route("/failed/<sname><int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry {sname.title()} ,you have failed with {marks} marks!</h1>"




@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num <30:
        #redirect to failed page
        return redirect(url_for("failed",sname=name,marks=num))#function
    else:
    #redirecting to passed page
        return redirect(url_for("passed",sname=name,marks=num))

if __name__=="__main__":
    app.run(debug=True)