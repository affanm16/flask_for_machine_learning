from flask import Flask , redirect, url_for
app= Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/pass")
def passed():
    return "<h1>Congrats you have passed</h1>"

@app.route("/failed")
def failed():
    return "<h1>Sorry you have passed</h1>"




@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num <30:
        #redirect to failed page
        return redirect(url_for("failed"))#function
    else:
    #redirecting to passed page
        return redirect(url_for("passed"))

if __name__=="__main__":
    app.run(debug=True)