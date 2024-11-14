from flask import Flask
app3 = Flask(__name__) #app3
from flask import request, render_template
@app3.route("/", methods = ["GET", "POST"]) #app3
def i():
    if request.method == "POST": #post?
        num = float(request.form.get("rates"))  #rates: html里的name
        return(render_template("index2.html", result = 90.2-(50.6*num))) #result: html里的变量
    else:
        return render_template("index2.html", result ="Waiting……….")
if __name__=="__main__":
    app3.run() #app3
