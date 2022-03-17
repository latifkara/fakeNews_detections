import joblib
from flask import Flask,render_template,request

import OzellikCikarma
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")



@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        data = OzellikCikarma.getAttributess(url)
        try:
            loaded_rf = joblib.load("./random_forest.joblib")

        except:
            print("hata oluştu")

        predicted_value = loaded_rf.predict(data)
        #print(predicted_value)
        if predicted_value == 0:
            value = "yasal"
            return render_template("main.html",error=value)
        else:
            value = "Sahte"
            return render_template("main.html",error=value)
if __name__ == "__main__":
    app.run(debug=True)