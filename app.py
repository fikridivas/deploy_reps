from flask import Flask, request ,render_template,jsonify
import streamlit as st
import pickle

app=Flask(__name__)

#load model
model_file=open('fix.pkl','rb')
model=pickle.load(model_file,encoding='bytes')

#make the route
@app.route('/')

def index():
    return render_template('deploy.html',pm10="0",pm25='0',so2='0',co='0',o3='0',no2='0',air_quality='Normal')

@app.route('/predict',methods=['POST'])

def predict():
    #predict air quality from air index
    # pm10,pm25,so2,co,o3,no2=[x for x in request.form.values()]

    # data=[]
    # #add data from form values
    # data.append(float(pm10))
    # data.append(float(pm25))
    # data.append(float(so2))
    # data.append(float(co))
    # data.append(float(o3))
    # data.append(float(no2))
    pm10=int(request.form['pm10'])
    pm25=int(request.form['pm25'])
    so2=int(request.form['so2'])
    co=int(request.form['co'])
    o3=int(request.form['o3'])
    no2=int(request.form['no2'])

    prediction=model.predict([[pm10,pm25,so2,co,o3,no2]])
    output=prediction[0]
    # if prediction[0]==0:
    #     output=="Bagus"
    # elif prediction[0]==1:
    #     output=="Sedang"
    # elif prediction[0]=="2":
    #     output=="Jelek"

    return render_template('deploy.html',pm10=pm10,pm25=pm25,so2=so2,co=co,o3=o3,no2=no2,air_quality=output)
if __name__=='__main__':
    app.run(debug=False)
