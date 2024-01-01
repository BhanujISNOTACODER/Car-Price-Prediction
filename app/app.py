from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

cars = pickle.load(open('../exports/cardDict.pkl','rb'))
cars = pd.DataFrame(cars)
model = pickle.load(open('../exports/model.pkl','rb'))


@app.route('/')
def home():
    manu = sorted(cars['Make'].unique())
    model = sorted(cars['Model'].unique())
    year = sorted(cars['Year'].unique())
    mileage = sorted(cars['Mileage'].unique())

    return render_template('index.html',manu=manu,model=model,year=year,mileage=mileage)

@app.route('/process',methods=['POST'])
def process():
    manu = request.form.get('manu')
    CarModel = request.form.get('CarModel')
    year = int(request.form.get('year'))
    mileage = int(request.form.get('mileage'))

    predictionDF = pd.DataFrame([[manu,CarModel,year,mileage]],columns=["Make","Model","Year","Mileage"]);
    pred = model.predict(predictionDF)
    return str(np.round(pred[0][0],2))


if __name__ == '__main__':
    app.run(debug=True)