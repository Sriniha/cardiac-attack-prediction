#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from flask import Flask,request,render_template
import pickle


# In[4]:


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
model1=pickle.load(open('model1.pkl','rb'))
model2=pickle.load(open('model2.pkl','rb'))
model3=pickle.load(open('model3.pkl','rb'))
model4=pickle.load(open('model4.pkl','rb'))

# In[5]:


@app.route('/')
def home():
    return render_template('index.html')


# In[7]:


@app.route('/predict',methods=["POST"])
def predict():
    req=request.form
    l=[]
    for k,v in req.items():
        if k=="oldpeak":
            l.append(float(v))
            continue
        l.append(int(v))
        print(k)
    final_features=[np.array(l)]
    output=[]
    prediction=model.predict(final_features)
    output.append(prediction[0])

    model1.n_samples_fit_=len(l)
    prediction=model1.predict(final_features)
    output.append(prediction[0])
    
    prediction=model2.predict(final_features)
    output.append(prediction[0])

    #prediction=model3.predict(final_features)
    #output.append(prediction[0])

    #model1.n_samples_fit_=len(l)
    #prediction=model4.predict(final_features)
    #output.append(prediction[0])

    print(output)
    if output.count(0)>=1:
        res='Congratulation,Patient is Healthy'
    else:
        res='Heart disease may occur'
    return render_template('index.html',prediction_text=res)


if __name__=="__main__":
    app.run(debug=True)




