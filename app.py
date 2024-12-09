from flask import Flask
from flask import render_template, request
import textblob

app = Flask("__name__") ### 这里"app"最好和文件名一致，"__": 在手机上使用时如果有web scam, creater will look for you


@app.route("/",methods =["GET","POST"]) #/是staring point,
def index():
    return(render_template("index.html")) ###111

@app.route("/main",methods =["GET","POST"]) #/是staring point,
def main():
    name = request.form.get("q")
    return(render_template("main.html")) ###111

@app.route("/SA",methods =["GET","POST"]) #/是staring point,
def SA():
    return(render_template("SA.html")) ###111

@app.route("/SA_result",methods =["GET","POST"]) #/是staring point,
def SA_result():
    q = request.form.get("q")  #第一个q是back end in python. 第二个q是front end from html
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r)) ###111

if __name__ == "__main__": #magic name, "__": for system,我们不能用于variable name， double confirm：writing+responsible, responsable
    app.run() 



