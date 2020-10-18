from flask import Flask, redirect, url_for,Response, render_template, request
from login.extension import mongo
import json
from host import get_ip
from flask_pymongo import PyMongo 
app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MONGO_DNAME']='udemy_collect'
app.config['MONGO_URI']="mongodb+srv://test:test@cluster0-yro7g.mongodb.net/api_flask?retryWrites=true&w=majority"
mongo.init_app(app) #already initialized in extension.py
from login.login import login #import blueprint fromseprate folder
app.register_blueprint(login,url_prefix="/login") #register login file in main file 

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
    ip=get_ip()['ip']
    app.run(host=ip,debug=True)
