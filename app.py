import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.image(r'https://upload.wikimedia.org/wikipedia/en/thumb/2/27/Swiggy_logo_%28old%29.svg/960px-Swiggy_logo_%28old%29.svg.png')
st.title("Swiggy Delivery Time Prediction")

# -----------------------------------------
# LOAD MODEL
# -----------------------------------------
MODEL_PATH = "model_.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

feature_list = model.feature_names_in_

# -----------------------------------------
# INPUTS
# -----------------------------------------
st.subheader("Enter Order Details")

age = st.number_input("Rider Age", 18, 60, 25)
ratings = st.slider("Rider Rating", 1.0, 5.0, 4.0)

traffic_label = st.selectbox(
    "Traffic",
    ["low", "medium", "high", "jam"]
)
traffic_map = {"low": 0, "medium": 1, "high": 2, "jam": 3}
traffic = traffic_map[traffic_label]

vehicle_condition = st.selectbox(
    "Vehicle Condition",
    [0, 1, 2],
    format_func=lambda x: ["Poor", "Average", "Good"][x]
)

type_of_vehicle = st.selectbox(
    "Type of Vehicle",
    ["motorcycle", "scooter", "electric_scooter"]
)

type_of_order = st.selectbox(
    "Type of Order",
    ["snack", "meal", "drinks", "buffet"]
)

weather = st.selectbox(
    "Weather Condition",
    ["sunny", "cloudy", "fog", "stormy", "sandstorms"]
)

multiple_deliveries = st.selectbox(
    "Multiple Deliveries",
    [1, 2, 3]
)

city_type = st.selectbox(
    "City Type",
    ["urban", "metropolitan"]
)

city_name = st.selectbox(
    "City",
    ["BANG", "HYD", "CHEN", "MUM", "PUNE", "DEL"]
)

pickup_time_minutes = st.number_input("Pickup Time (minutes)", 1, 60, 12)
order_time_hour = st.number_input("Order Time Hour", 0, 23, 10)
distance = st.number_input("Distance (km)", 0.1, 50.0, 5.0)

is_weekend = st.selectbox(
    "Is Weekend?",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# -----------------------------------------
# BUILD INPUT DATAFRAME (ONE-HOT SAFE)
# -----------------------------------------
input_data = pd.DataFrame(
    np.zeros((1, len(feature_list))),
    columns=feature_list
)

def set_val(col, val):
    if col in input_data.columns:
        input_data.at[0, col] = val

# Numeric
set_val("age", age)
set_val("ratings", ratings)
set_val("traffic", traffic)
set_val("vehicle_condition", vehicle_condition)
set_val("multiple_deliveries", multiple_deliveries)
set_val("pickup_time_minutes", pickup_time_minutes)
set_val("order_time_hour", order_time_hour)
set_val("distance", distance)
set_val("is_weekend", is_weekend)

# One-hot categorical
set_val(f"type_of_vehicle_{type_of_vehicle}", 1)
set_val(f"type_of_order_{type_of_order}", 1)
set_val(f"weather_{weather}", 1)
set_val(f"city_type_{city_type}", 1)
set_val(f"city_name_{city_name}", 1)

# -----------------------------------------
# PREDICTION
# -----------------------------------------
if st.button("Predict Delivery Time"):
    prediction = model.predict(input_data)[0]
    st.success(f"⏱ Estimated Delivery Time: {prediction:.2f} minutes")