from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_winequality():
    fixed_acidity=float(request.form.get("fixed_acidity"))
    volatile_acidity=float(request.form.get("volatile_acidity"))
    citric_acid=float(request.form.get("citric_acid"))
    Residual_sugar=float(request.form.get("Residual_sugar"))
    chlorides=float(request.form.get("chlorides"))
    sulfur_dioxide=float(request.form.get("sulfur_dioxide"))
    total_sulfur_dioxide=float(request.form.get("total_sulfur_dioxide"))
    Density=float(request.form.get("Density"))
    ph=float(request.form.get("ph"))
    sulphates=float(request.form.get("sulphates"))
    alcohol=float(request.form.get("alcohol"))

    
    
    
    result=model.predict(np.array([[fixed_acidity,volatile_acidity,citric_acid,Residual_sugar,chlorides,sulfur_dioxide,total_sulfur_dioxide,Density,ph,sulphates,alcohol]]))
    
    if result[0]==3:
        return "<h1 style='color:green'>GOOD WINE QUALITY</h1>"
    else:
        return "<h1 style='color:red'>BAD WINE QUALITY</h1>"
    
    
# @app.route("/predict",methods=["GET"])
# def predict_placement():
#     cgpa=float(request.args.get("cgpa"))
#     iq=float(request.args.get("iq"))
#     profile_score=float(request.args.get("profile_score"))
    
    
#     result=model.predict(np.array([[cgpa,iq,profile_score]]))
    
#     if result[0]==1:
#         return "<h1 style='color:green'>PLACED</h1>"
#     else:
#         return "<h1 style='color:red'>NOT PLACED</h1>"




##############################################################################
##############################################################################   
##############################################################################
##############################################################################

app.run(debug=True,port=5002)