from sqlalchemy import create_engine
import pandas as pd
import os
import json

engine = create_engine(os.environ.get("JAWSDB_URL"))

latlon_df = pd.read_sql("SELECT * FROM LatLon_Table", engine)

# CO2 emissions API
with open('static/data/countries.geojson', 'r') as f:
    countries_co2_emissions = json.load(f)

CO2_emissions_df = pd.read_sql("SELECT * FROM CO2_Emissions", engine)
CO2_emissions_df_merged = CO2_emissions_df.merge(latlon_df, how='inner', on='Country')
CO2_emissions_json = json.loads(CO2_emissions_df_merged.to_json(orient="records"))
# # Loop over GeoJSON features and add the new properties
# print(countries_co2_emissions['features'][0])
# for feat in countries_co2_emissions['features']:
#     value_1990 = "NA"
#     value_2000 = "NA"
#     value_2010 = "NA"
#     value_2017 = "NA"
#     for i in range(len(CO2_emissions_json)):
#         dict = CO2_emissions_json[i]
#         if dict['Country'] == feat['properties']["ADMIN"]:
#             value_1990 = dict["1990"]
#             value_2000 = dict["2000"]
#             value_2010 = dict["2010"]
#             value_2017 = dict["2017"]
            
#     if value_2017 == "NA":
#         del feat
#     else:
#         feat['properties']["1990"] = value_1990
#         feat['properties']["2000"] = value_2000
#         feat['properties']["2010"] = value_2010
#         feat['properties']["2017"] = value_2017

#Create list of countries in from CO2_emissions_json
country_list = []
for i in range(len(CO2_emissions_json)):
    country_list.append(CO2_emissions_json[i]['Country'].upper())

# for some this for loop won't remove all entries in single run 
# so I have forced it to run 10 times :)
for i in range(10):
    for feat in countries_co2_emissions['features']:
        if feat['properties']["ADMIN"].upper() not in country_list:
            countries_co2_emissions['features'].remove(feat)

# Remove List of countries from countries_co2_emissions i.e. geojson

for feat in countries_co2_emissions['features']:
    for i in range(len(CO2_emissions_json)):
        dict1 = CO2_emissions_json[i]
        if dict1['Country'].upper() == feat['properties']["ADMIN"].upper():
            feat['properties']["1990"] = dict1["1990"]
            feat['properties']["2000"] = dict1["2000"]
            feat['properties']["2010"] = dict1["2010"]
            feat['properties']["2017"] = dict1["2017"]

CO2_emissions_api = countries_co2_emissions

    # if value_2000 != "NA":
    #     feat['properties']["2000"] = value_2000
    # # else:
    # #     del feat

    # if value_2010 != "NA":
    #     feat['properties']["2010"] = value_2010
    # # else:
    # #     del feat

    # if value_2017 != "NA":
    #     feat['properties']["2017"] = value_2017
    # # else:
    # #     del feat

CO2_emissions_api = countries_co2_emissions

# crude/NGL production API
with open('static/data/countries.geojson', 'r') as f:
    countries_NGL_prod = json.load(f)

Crude_NGL_Prod_df = pd.read_sql("SELECT * FROM Crude_NGL_Production", engine)
Crude_NGL_Prod_df_merged=Crude_NGL_Prod_df.merge(latlon_df,how='inner',on='Country')
Crude_NGL_Prod_json = json.loads(Crude_NGL_Prod_df_merged.to_json(orient = "records"))
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
with open('static/data/countries.geojson', 'r') as f:
    countries_nat_gas_prod = json.load(f)

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

# Renewable Share Production API
with open('static/data/countries.geojson', 'r') as f:
    countries_ren_elec_share = json.load(f)

Renewables_Electricity_Share_df = pd.read_sql("SELECT * FROM Renewables_Electricity_Share", engine)
Renewables_Electricity_Share_df_merged=Renewables_Electricity_Share_df.merge(latlon_df,how='inner',on='Country')
Renewables_Electricity_Share_json = json.loads(Renewables_Electricity_Share_df_merged.to_json(orient = "records"))
# Loop over GeoJSON features and add the new properties
for feat in countries_ren_elec_share['features']:
    value_1990 = "NA"
    value_2000 = "NA"
    value_2010 = "NA"
    value_2017 = "NA"
    for i in range(len(Renewables_Electricity_Share_json)):
        dict = Renewables_Electricity_Share_json[i]
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

Renewables_Electricity_Share_api = countries_ren_elec_share

# solar wind share API
with open('static/data/countries.geojson', 'r') as f:
    countries_solar_wind_share = json.load(f)

Solar_and_Wind_Share_df = pd.read_sql("SELECT * FROM Solar_and_Wind_Share", engine)
Solar_and_Wind_Share_df_merged=Solar_and_Wind_Share_df.merge(latlon_df,how='inner',on='Country')
Solar_and_Wind_Share_json = json.loads(Solar_and_Wind_Share_df_merged.to_json(orient = "records"))
# Loop over GeoJSON features and add the new properties
for feat in countries_solar_wind_share['features']:
    value_1990 = "NA"
    value_2000 = "NA"
    value_2010 = "NA"
    value_2017 = "NA"
    for i in range(len(Solar_and_Wind_Share_json)):
        dict = Solar_and_Wind_Share_json[i]
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

Solar_and_Wind_Share_api = countries_solar_wind_share

# total elec production API
with open('static/data/countries.geojson', 'r') as f:
    countries_total_elec_prod = json.load(f)

Total_Electricity_Prod_df = pd.read_sql("SELECT * FROM Total_Electricity_Production", engine)
Total_Electricity_Prod_df_merged=Total_Electricity_Prod_df.merge(latlon_df,how='inner',on='Country')
Total_Electricity_Prod_json = json.loads(Total_Electricity_Prod_df_merged.to_json(orient = "records"))
# Loop over GeoJSON features and add the new properties
for feat in countries_total_elec_prod['features']:
    value_1990 = "NA"
    value_2000 = "NA"
    value_2010 = "NA"
    value_2017 = "NA"
    for i in range(len(Total_Electricity_Prod_json)):
        dict = Total_Electricity_Prod_json[i]
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

Total_Electricity_Prod_api = countries_total_elec_prod