from flask import Flask, jsonify, render_template, request
import pandas
from JSONify_APIs import CO2_emissions_api, Crude_NGL_Prod_api, Natural_Gas_Prod_api, Renewables_Electricity_Share_api, Solar_and_Wind_Share_api, Total_Electricity_Prod_api
import json

app = Flask(__name__)

@app.route("/newmap")
def new():
  """Energy Evolution"""
  return render_template("index2.html")

@app.route("/")
def index():
    """Energy Evolution"""
    return render_template("index.html")

#api route for data to go to client
@app.route("/ee/co2")
def co2():
    return jsonify(CO2_emissions_api)

@app.route("/ee/liquids")
def ngl():
    return jsonify(Crude_NGL_Prod_api)

@app.route("/ee/gas")
def gas():
    return jsonify(Natural_Gas_Prod_api)

@app.route("/ee/renewables")
def renew():
    return jsonify(Renewables_Electricity_Share_api)

@app.route("/ee/solar_wind")
def solar():
    return jsonify(Solar_and_Wind_Share_api)

@app.route("/ee/total")
def total():
    return jsonify(Total_Electricity_Prod_api)

if __name__ == "__main__":
    app.run()


