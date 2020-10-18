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

@login.route("/add",methods=['POST'])
def add_data():
    if request.method=="POST":
        name=str(request.form['u_name'])
        email=str(request.form['email'])
        password=str(request.form['password'])
        data=mongo.db.user_data
        q=data.find_one({"email":email})
        if q:
            return "<h1> email already registered</h1>"
        else:
            entery_id=data.insert({'name':name,'email':email,'password':password})
            get_data=data.find_one({"_id":entery_id})
            r_name=get_data['name']
            r_email=get_data['email']
            output={'name':get_data['name'],'email':get_data['email']}#'password':get_data['password']}
            result= "Welcome "+str(r_name) +", your email id: "+str(r_email)+" is registered."    
            return render_template("welcome_page.html",content=result)
    #return jsonify({'result':output})

@login.route("/",methods=['GET','POST']) #name of module refrenced 
def login_page():
    if request.method=="POST":
        #name=str(request.form["u_name"])
        email=str(request.form["email"])
        password=str(request.form["password"])
        data=mongo.db.user_data
        q= data.find_one({"email":email})
        if q:
            if q['password'] == password:
                r_name=q['name']
                output="Welcome back "+str(r_name)+", you are logged in"
                return output
            else:
                return "<h1> Wrong Password </h1>"
        else:
            return "<h1> Cant find you, Kindly sign up </h1>"    
    else:
        return render_template("login.html")