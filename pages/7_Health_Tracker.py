# pages/7_Health_Tracker.py
import streamlit as st
import datetime

st.set_page_config(page_title="Health Tracker - HealPoint", page_icon="📈")
st.title("📈 Health Tracker")

st.sidebar.success("Logged in as Patient")

st.subheader("🔢 Input Your Vitals")
date = st.date_input("Date", datetime.date.today())
bp = st.text_input("Blood Pressure (e.g., 120/80)")
sugar = st.text_input("Blood Sugar Level (mg/dL)")
weight = st.text_input("Weight (kg)")

if st.button("Save Record"):
    st.success("Health record saved!")

st.markdown("---")

st.subheader("📊 Sample History")
st.line_chart({
    "Blood Sugar": [110, 108, 115, 130],
    "Weight": [60, 60.5, 61, 61.2]
})

st.write("📅 Dates: 25 July, 27 July, 30 July, 2 Aug")
