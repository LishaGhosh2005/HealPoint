# pages/4_Patient_Dashboard.py
import streamlit as st

st.set_page_config(page_title="Patient Dashboard - HealPoint", page_icon="🩺")
st.title("🩺 Patient Dashboard")

st.sidebar.success("Logged in as Patient")

st.subheader("📅 My Appointments")
st.write("- 3 Aug, 2025 — Dr. Rahul Sengupta (Cardiologist) at 3:00 PM")
st.write("- 10 Aug, 2025 — Dr. Anjali Mehra (General Physician) at 11:00 AM")

st.subheader("📤 Upload Reports")
report = st.file_uploader("Upload Medical Report", type=["pdf", "jpg", "png"])
if report:
    st.success("Report uploaded successfully!")

st.subheader("📄 View Prescriptions")
st.write("- 3 Aug, 2025 — *Take Atorvastatin daily for cholesterol.*")
st.write("- 15 Jul, 2025 — *Antibiotics for throat infection*")

st.subheader("📚 My Health Records")
st.write("- Blood Pressure: 120/80 mmHg\n- Blood Sugar: 92 mg/dL (Fasting)\n- Weight: 60 kg")

st.subheader("🧪 Book Test / View Lab Results")
st.write("- CBC — Done — Result: Normal")
st.write("- Thyroid — Pending")

st.subheader("💬 Doctor's Advice")
st.write("- Dr. Anjali: *Maintain low salt diet and walk 30 mins daily.*")

st.subheader("📱 Emergency Contacts")
st.write("- Emergency: 112\n- Hospital: 033-2460-1234")

st.subheader("💊 Medicine Reminders")
st.write("- Atorvastatin — 9:00 PM daily")

st.subheader("⚙️ Profile Settings")
st.text_input("Update Name")
st.text_input("Update Phone Number")
st.button("Save Changes")
