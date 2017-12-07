from flask import Flask, render_template, jsonify
from data import data
import requests
import json

app = Flask(__name__)

data = data()

@app.route('/')
@app.route('/home')
def homepage():
   return render_template("home.html", data=data)
   
@app.route('/test')
def testAPI():

   try:
      r = requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_INTRADAY&symbol=BTC&market=AUD&apikey=QY1GOJ78M3026VJH')
   except requests.ConnectionError:
      return "Connection Error"
   
   jsonData = r.text
   jsonToPython = json.loads(jsonData)
   return render_template("displayInfo.html", data=jsonToPython)

   
   
if __name__ == "__main__":
   app.run(debug=True)
   
