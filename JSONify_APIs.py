from sqlalchemy import create_engine
import pandas as pd
import os
import json

engine = create_engine(os.environ.get("JAWSDB_URL"))

with open('static/data/countries.geojson', 'r') as f:
    countries_co2_emissions = json.load(f)
    countries_NGL_prod = json.load(f)
    countries_nat_gas_prod = json.load(f)
    countries_solar_wind_share = json.load(f)
    countries_total_elec_prod = json.load(f)

latlon_df = pd.read_sql("SELECT * FROM LatLon_Table", engine)

# CO2 emissions API
CO2_emissions_df = pd.read_sql("SELECT * FROM CO2_Emissions", engine)
CO2_emissions_df_merged = CO2_emissions_df.merge(latlon_df, how='inner', on='Country')
CO2_emissions_json = json.loads(CO2_emissions_df_merged.to_json(orient="records"))

# Loop over GeoJSON features and add the new properties
for feat in countries_co2_emissions['features']:
    value_1990 = "NA"
    value_2000 = "NA"
    value_2010 = "NA"
    value_2017 = "NA"
    for i in range(len(CO2_emissions_json)):
        dict = CO2_emissions_json[i]
        if dict['Country'] == feat['properties']["ADMIN"]:
            value_1990 = dict["1990"]
            value_2000 = dict["2000"]
            value_2010 = dict["2010"]
            value_2017 = dict["2017"]
    if value_1990:
        feat['properties']["1990"] = value_1990
    if value_2000:
        feat['properties']["2000"] = value_2000
    if value_2010:
        feat['properties']["2010"] = value_2010
    if value_2017:
        feat['properties']["2017"] = value_2017

CO2_emissions_api = countries_co2_emissions

# crue/NGL production API
Crude_NGL_Prod_df = pd.read_sql("SELECT * FROM Crude_NGL_Production", engine)
Crude_NGL_Prod_df_merged=Crude_NGL_Prod_df.merge(latlon_df,how='inner',on='Country')
Crude_NGL_Prod_json = json.load(Crude_NGL_Prod_df_merged.to_json(orient = "records"))

# Loop over GeoJSON features and add the new properties
for feat in countries_NGL_prod['features']:
    value_1990 = "NA"
    value_2000 = "NA"
    value_2010 = "NA"
    value_2017 = "NA"
    for i in range(len(Crude_NGL_Prod_json)):
        dict = Crude_NGL_Prod_json[i]
        if dict['Country'] == feat['properties']["ADMIN"]:
            value_1990 = dict["1990"]
            value_2000 = dict["2000"]
            value_2010 = dict["2010"]
            value_2017 = dict["2017"]
    if value_1990:
        feat['properties']["1990"] = value_1990
    if value_2000:
        feat['properties']["2000"] = value_2000
    if value_2010:
        feat['properties']["2010"] = value_2010
    if value_2017:
        feat['properties']["2017"] = value_2017

Crude_NGL_Prod_api = countries_NGL_prod

# Natural Gas Prod API
Natural_Gas_Prod_df = pd.read_sql("SELECT * FROM Natural_Gas_Production", engine)
Natural_Gas_Prod_df_merged=Natural_Gas_Prod_df.merge(latlon_df,how='inner',on='Country')
Natural_Gas_Prod_json = json.loads(Natural_Gas_Prod_df_merged.to_json(orient = "records"))

# Loop over GeoJSON features and add the new properties
for feat in countries_nat_gas_prod['features']:
    value_1990 = "NA"
    value_2000 = "NA"
    value_2010 = "NA"
    value_2017 = "NA"
    for i in range(len(Natural_Gas_Prod_json)):
        dict = Natural_Gas_Prod_json[i]
        if dict['Country'] == feat['properties']["ADMIN"]:
            value_1990 = dict["1990"]
            value_2000 = dict["2000"]
            value_2010 = dict["2010"]
            value_2017 = dict["2017"]
    if value_1990:
        feat['properties']["1990"] = value_1990
    if value_2000:
        feat['properties']["2000"] = value_2000
    if value_2010:
        feat['properties']["2010"] = value_2010
    if value_2017:
        feat['properties']["2017"] = value_2017

Natural_Gas_Prod_api = countries_nat_gas_prod

# Renewables_Electricity_Share_df = pd.read_sql("SELECT * FROM Renewables_Electricity_Share", engine)
# Renewables_Electricity_Share_df_merged=Renewables_Electricity_Share_df.merge(latlon_df,how='inner',on='Country')
# Renewables_Electricity_Share_json = json.loads(Renewables_Electricity_Share_df_merged.to_json(orient = "records"))

# Solar_and_Wind_Share_df = pd.read_sql("SELECT * FROM Solar_and_Wind_Share", engine)
# Solar_and_Wind_Share_df_merged=Solar_and_Wind_Share_df.merge(latlon_df,how='inner',on='Country')
# Solar_and_Wind_Share_json = json.loads(Solar_and_Wind_Share_df_merged.to_json(orient = "records"))

# Total_Electricity_Prod_df = pd.read_sql("SELECT * FROM Total_Electricity_Production", engine)
# Total_Electricity_Prod_df_merged=Total_Electricity_Prod_df.merge(latlon_df,how='inner',on='Country')
# Total_Electricity_Prod_json = json.loads(Total_Electricity_Prod_df_merged.to_json(orient = "records"))
