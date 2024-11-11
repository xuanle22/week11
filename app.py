from flask import Flask
from flask import render_template, request

app = Flask("__name__") ### handphone, app和文件名重，和colab有区别？？


@app.route("/",methods =["GET","POST"]) #/是staring point,
def index():
    return(render_template("index.html")) ###111

if __name__ == "__main__": #magic name, double confirm, responsable
    app.run() 



