#create seprate folder for each blueprint and create __init__.py file
from flask import Flask, Blueprint, render_template,Response,request


login=Blueprint("login",__name__,static_folder="C:/Users/arsal/Desktop/anaconda/procure_me_v2/login/static",template_folder="C:/Users/arsal/Desktop/anaconda/procure_me_v2/login/templates") 
#initiate file with blueprint, keep name consistent 
#Blueprint("name",__name__, staic_folder,template_folder) 

@login.route("/",methods=['GET','POST']) #name of module refrenced 
def login_page():
    if request.method=="POST":
        name=str(request.form["u_name"])
        email=str(request.form["email"])
        password=str(request.form["password"])
        return f"{name} {email} {password}"

    return render_template("login.html")