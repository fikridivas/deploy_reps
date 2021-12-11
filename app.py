from flask import Flask, request ,render_template,jsonify
import streamlit as st
import pickle

app=Flask(__name__)

#load model
model_file=open('mantab.pkl','rb')
model=pickle.load(model_file,encoding='bytes')

#make the route
@app.route('/')

def index():
    return render_template('deploy.html',pm10="0",pm25='0',so2='0',co='0',o3='0',no2='0',air_quality='Normal')

@app.route('/predict',methods=['POST'])
def __init__(self,pm10,pm25,so2,co,o3,no2):
    self.pm10=pm10
    self.pm25=pm25
    self.so2=so2
    self.co=co
    self.o3=o3
    self.no2=no2

def predict(self):
    #predict air quality from air index
#     pm10,pm25,so2,co,o3,no2=[x for x in request.form.values()]

#     data=[]
    #add data from form values
#     data.append(int(pm10))
#     data.append(int(pm25))
#     data.append(int(so2))
#     data.append(int(co))
#     data.append(int(o3))
#     data.append(int(no2))
    self.pm10=int(request.form['pm10'])
    self.pm25=int(request.form['pm25'])
    self.so2=int(request.form['so2'])
    self.co=int(request.form['co'])
    self.o3=int(request.form['o3'])
    self.no2=int(request.form['no2'])

    prediction=model.predict([[self.pm10,self.pm25,self.so2,self.co,self.o3,self.no2]])
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
