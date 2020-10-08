#create seprate folder for each blueprint and create __init__.py file
from flask import Flask, Blueprint, render_template,Response,request
from flask import jsonify,redirect, url_for
from .extension import mongo #create extension method as in https://stackoverflow.com/questions/28784849/how-to-fix-circular-import-in-flask-project-using-blueprints-mysql-w-o-sqlalchemx#new-answer
# first import in main app.py and than call here from extension

login=Blueprint("login",__name__,static_folder="C:/Users/arsal/Desktop/anaconda/procure_me_v2/login/static",template_folder="C:/Users/arsal/Desktop/anaconda/procure_me_v2/login/templates") 
#initiate file with blueprint, keep name consistent 
#Blueprint("name",__name__, staic_folder,template_folder) 



@login.route("/data",methods=['GET'])
def all_data():
    data=mongo.db.user_data #connect to test collection in mongodb udemy_collect
    output=[]
    for i in data.find():
        output.append({"name":i['name'],"age":i['age']})
    return jsonify({"result":output})

@login.route("/",methods=['GET','POST']) #name of module refrenced 
def login_page():
    if request.method=="POST":
        name=str(request.form["u_name"])
        email=str(request.form["email"])
        password=str(request.form["password"])
        return f"{name} {email} {password}"

    return render_template("login.html")