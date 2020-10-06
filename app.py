from flask import Flask, redirect, url_for,Response, render_template, request
from login.login import login #import blueprint fromseprate folder
app=Flask(__name__)
app.register_blueprint(login,url_prefix="/login") #register login file in main file 
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/",methods=["GET"])
def home():
    return render_template("home.html")




@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Expires'] = '-1'
    return response

if __name__=="__main__":
    app.run(host="192.168.1.104",debug=True)
