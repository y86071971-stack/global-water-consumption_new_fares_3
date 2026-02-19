import streamlit as st
import joblib
model = joblib.load("C:/Users/PC1/Desktop/fares/model_to_fares.pkl")
sc= joblib.load("C:/Users/PC1/Desktop/fares/sc_to_fares.pkl")
le= joblib.load("C:/Users/PC1/Desktop/fares/le_Water_Scarcity_to_fares_Level.pkl")


water=st.number_input("water:",step=1.00)

PerCapit=st.number_input("Per Capit:",step=1.00)

AgriculturalWaterUse=st.number_input("Agricultural Water Use:",step=1.00)

IndustrialWaterUse=st.number_input("Industrial Water Use:",step=1.00)

HouseholdWaterUse=st.number_input("Household Water Use:",step=1.00)

RainfallImpact=st.number_input("Rainfall Impact:",step=1.00)

GroundwaterDepletionRate=st.number_input("Groundwater Depletion Rate:",step=1.00)


input_scale=sc.transform([[water,PerCapit,AgriculturalWaterUse,IndustrialWaterUse,HouseholdWaterUse,RainfallImpact,GroundwaterDepletionRate]])
WaterScarcityLevel=model.predict(input_scale)
st.success(WaterScarcityLevel)