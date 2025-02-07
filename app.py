# API can not appear in cloud
from flask import Flask
from flask import render_template, request
import textblob
import google.generativeai as genai
import os

api = os.getenv("makersuite")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")
#####

app = Flask("__name__") ### 这里"app"最好和文件名一致，"__": 在手机上使用时如果有web scam, creater will look for you


@app.route("/",methods =["GET","POST"]) #/是staring point,
def index():
    return(render_template("index.html")) ###111

@app.route("/main",methods =["GET","POST"]) 
def main():
    name = request.form.get("q")
    return(render_template("main.html")) 

@app.route("/SA",methods =["GET","POST"]) 
def SA():
    return(render_template("SA.html")) 

@app.route("/SA_result",methods =["GET","POST"]) 
def SA_result():
    q = request.form.get("q")  #第一个q是back end in python. 第二个q是front end from html
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r)) 


@app.route("/genAI",methods =["GET","POST"]) 
def genAI():
    return(render_template("genAI.html")) 

@app.route("/genAI_result",methods =["GET","POST"]) 
def genAI_result():
    q = request.form.get("q") 
    r = model.generate_content(q)
    return(render_template("genAI_result.html",r=r.candidates[0].content.parts[0].text)) ###111

@app.route("/paynow",methods =["GET","POST"]) 
def paynow():
    return(render_template("paynow.html")) 

if __name__ == "__main__": #magic name, "__": for system,我们不能用于variable name， double confirm：writing+responsible, responsable
    app.run() 



