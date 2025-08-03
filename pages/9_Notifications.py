# pages/9_Notifications.py
import streamlit as st
import datetime

st.set_page_config(page_title="Notifications - HealPoint", page_icon="🔔")
st.title("🔔 Notifications Center")

st.sidebar.success("Stay Informed")

st.markdown("### 📆 Upcoming Reminders")
st.info("🕐 4 Aug 2025, 10:00 AM - Appointment with Dr. Anjali Mehra")
st.info("💊 4 Aug 2025, 8:00 AM - Take Blood Pressure Medicine")

st.markdown("---")

st.markdown("### ✅ Recent Updates")
st.success("🧪 CBC Test Result Available - 3 Aug 2025")
st.success("📩 Message from Dr. Rahul Sengupta - 2 Aug 2025")
st.success("📄 New Prescription Uploaded - 1 Aug 2025")

st.markdown("---")

st.caption("🔁 This is dummy data. You can replace with real-time backend alerts later.")
