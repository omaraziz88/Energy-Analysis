from sqlalchemy import create_engine
import pandas as pd
import os
engine = create_engine(os.environ.get("JAWSDB_URL"))

latlon_df = pd.read_sql("SELECT * FROM LatLon_Table", engine)
CO2_emissions_df = pd.read_sql("SELECT * FROM CO2_Emissions", engine)
CO2_emissions_df_merged=CO2_emissions_df.merge(latlon_df,how='inner',on='Country')
CO2_emissions_api = CO2_emissions_df_merged.to_json(orient = "records")

Crude_NGL_Prod_df = pd.read_sql("SELECT * FROM Crude_NGL_Production", engine)
Crude_NGL_Prod_df_merged=Crude_NGL_Prod_df.merge(latlon_df,how='inner',on='Country')
Crude_NGL_Prod_api = Crude_NGL_Prod_df_merged.to_json(orient = "records")

Natural_Gas_Prod_df = pd.read_sql("SELECT * FROM Natural_Gas_Production", engine)
Natural_Gas_Prod_df_merged=Natural_Gas_Prod_df.merge(latlon_df,how='inner',on='Country')
Natural_Gas_Prod_api = Natural_Gas_Prod_df_merged.to_json(orient = "records")

Renewables_Electricity_Share_df = pd.read_sql("SELECT * FROM Renewables_Electricity_Share", engine)
Renewables_Electricity_Share_df_merged=Renewables_Electricity_Share_df.merge(latlon_df,how='inner',on='Country')
Renewables_Electricity_Share_api = Renewables_Electricity_Share_df_merged.to_json(orient = "records")

Solar_and_Wind_Share_df = pd.read_sql("SELECT * FROM Solar_and_Wind_Share", engine)
Solar_and_Wind_Share_df_merged=Solar_and_Wind_Share_df.merge(latlon_df,how='inner',on='Country')
Solar_and_Wind_Share_api = Solar_and_Wind_Share_df_merged.to_json(orient = "records")

Total_Electricity_Prod_df = pd.read_sql("SELECT * FROM Total_Electricity_Production", engine)
Total_Electricity_Prod_df_merged=Total_Electricity_Prod_df.merge(latlon_df,how='inner',on='Country')
Total_Electricity_Prod_api = Total_Electricity_Prod_df_merged.to_json(orient = "records")


# api_1 = df1.to_json(orient = "records")

# df2 = pd.read_sql("SELECT * FROM Crude_NGL_Production", engine)
# api_2 = df2.to_json(orient = "records")

# df3 = pd.read_sql("SELECT * FROM Renewables_Electricity_Share", engine)
# api_3 = df3.to_json(orient = "records")

# df4 = pd.read_sql("SELECT * FROM Solar_and_Wind_Share", engine)
# api_4 = df4.to_json(orient = "records")

# df5 = pd.read_sql("SELECT * FROM Total_Electricity_Production", engine)
# api_5 = df5.to_json(orient = "records")