from flask import Flask
from flask import render_template, request

app = Flask("__name__") ### 这里"app"最好和文件名一致，"__": 在手机上使用时如果有web scam, creater will look for you


@app.route("/",methods =["GET","POST"]) #/是staring point,
def index():
    return(render_template("index.html")) ###111

@app.route("/main",methods =["GET","POST"]) #/是staring point,
def main():
    name = request.form.get("q")
    return(render_template("main.html")) ###111

if __name__ == "__main__": #magic name, "__": for system,我们不能用于variable name， double confirm：writing+responsible, responsable
    app.run() 



