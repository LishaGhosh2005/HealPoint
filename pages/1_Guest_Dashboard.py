# pages/1_Guest_Dashboard.py
import streamlit as st

st.set_page_config(page_title="Guest Dashboard", page_icon="👤")
st.title("👤 Guest Dashboard")

st.markdown("""
Welcome to the HealPoint Guest Portal.

Here you can explore basic health information, doctor availability, and test pricing.
""")

st.subheader("🧑‍⚕️ Available Doctors")
doctors = [
    {"name": "Dr. Anjali Mehra", "dept": "General Physician", "avail": "Mon–Fri, 10am–4pm"},
    {"name": "Dr. Rahul Sengupta", "dept": "Cardiologist", "avail": "Tue–Thu, 2pm–6pm"},
    {"name": "Dr. Riya Sharma", "dept": "Gynecologist", "avail": "Mon–Wed, 11am–3pm"},
    {"name": "Dr. Farhan Ali", "dept": "Neurologist", "avail": "Sat–Sun, 12pm–4pm"},
    {"name": "Dr. Shweta Das", "dept": "Dermatologist", "avail": "Mon–Fri, 9am–1pm"}
]
for doc in doctors:
    st.markdown(f"**{doc['name']}** — *{doc['dept']}* — 🕒 {doc['avail']}")

st.subheader("🧪 Popular Lab Tests")
tests = [
    ("Complete Blood Count (CBC)", "₹500", "12 hrs"),
    ("Blood Sugar (Fasting)", "₹200", "6 hrs"),
    ("Lipid Profile", "₹700", "24 hrs"),
    ("ECG", "₹800", "1 hr"),
    ("Urine Test", "₹300", "8 hrs"),
    ("Pregnancy Test", "₹350", "2 hrs"),
    ("Thyroid Function Test", "₹600", "24 hrs")
]
for test in tests:
    st.markdown(f"**{test[0]}** — 💰 {test[1]} — 🕒 Result in {test[2]}")

st.info("Login or Signup to access full features like appointments, reports, and health tracking.")
