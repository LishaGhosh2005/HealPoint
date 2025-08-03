# pages/5_Doctor_Dashboard.py
import streamlit as st

st.set_page_config(page_title="Doctor Dashboard - HealPoint", page_icon="👨‍⚕️")
st.title("👨‍⚕️ Doctor Dashboard")

st.sidebar.success("Logged in as Doctor")

st.subheader("📅 Today's Appointments")
st.write("- 10:30 AM — Rina Das — Fever, cough")
st.write("- 12:00 PM — Amit Pal — Chest pain")

st.subheader("🗂️ Patient History")
patient = st.selectbox("Select Patient", ["Rina Das", "Amit Pal"])
if patient == "Rina Das":
    st.write("- Last Visit: 12 July 2025\n- Diagnosis: Viral Fever\n- Prescriptions: Paracetamol")
elif patient == "Amit Pal":
    st.write("- Last Visit: 5 June 2025\n- Diagnosis: High BP\n- Prescriptions: Amlodipine")

st.subheader("💊 Write Prescription")
selected_patient = st.selectbox("Choose Patient", ["Rina Das", "Amit Pal"], key="prescribe")
prescription = st.text_area("Prescription Notes")
if st.button("Submit Prescription"):
    if prescription:
        st.success(f"Prescription for {selected_patient} saved.")
    else:
        st.error("Please write something.")

st.subheader("📄 Upload Notes / Diagnosis")
notes = st.text_area("Enter Notes/Diagnosis")
if st.button("Upload Notes"):
    if notes:
        st.success("Notes uploaded.")
    else:
        st.error("Please enter something.")

st.subheader("📤 View Uploaded Reports")
st.write("- Rina Das — Blood Test Report.pdf")
st.write("- Amit Pal — ECG.jpeg")

st.subheader("📆 Schedule Availability")
day = st.selectbox("Day", ["Mon", "Tue", "Wed", "Thu", "Fri"])
time_slot = st.text_input("Time Slot (e.g., 10am–2pm)")
if st.button("Update Availability"):
    st.success(f"Availability updated: {day}, {time_slot}")

st.subheader("📊 Patient Stats Overview")
st.write("- Total Patients Today: 2\n- Average Consultation Time: 22 mins")

st.subheader("⚙️ Profile Settings")
st.text_input("Update Name")
st.text_input("Update Phone Number")
st.button("Save Changes")
