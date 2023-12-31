from flask import Flask, render_template
import pickle
import pandas as pd

app = Flask(__name__)

cars = pickle.load(open('../exports/cardDict.pkl','rb'))
cars = pd.DataFrame(cars)


@app.route('/')
def home():
    manu = sorted(cars['Make'].unique())
    model = sorted(cars['Model'].unique())
    year = sorted(cars['Year'].unique())
    mileage = sorted(cars['Mileage'].unique())
    def zip_lists(L1, L2):
        return list(zip(L1, L2))
    ManModel = zip_lists(manu,model)
    print(ManModel)

    return render_template('index.html',manu=manu,model=model,year=year,mileage=mileage,ManModel=ManModel)

if __name__ == '__main__':
    app.run(debug=True)