# pages/6_Lab_Tests.py
import streamlit as st

st.set_page_config(page_title="Lab Test Booking - HealPoint", page_icon="🧪")
st.title("🧪 Book a Lab Test")

st.sidebar.success("Logged in as Patient")

st.subheader("Available Tests")
tests = {
    "Complete Blood Count (CBC)": ("Pathology", "₹500", "12 hrs"),
    "Blood Sugar (Fasting)": ("Diabetology", "₹200", "6 hrs"),
    "Lipid Profile": ("Cardiology", "₹700", "24 hrs"),
    "ECG": ("Cardiology", "₹800", "1 hr"),
    "Urine Test": ("General Diagnosis", "₹300", "8 hrs"),
    "Pregnancy Test": ("Gynaecology", "₹350", "2 hrs"),
    "Thyroid Function Test": ("Endocrinology", "₹600", "24 hrs")
}

test_choice = st.selectbox("Choose a Test", list(tests.keys()))
department, cost, time = tests[test_choice]

st.write(f"**Department:** {department}")
st.write(f"**Cost:** {cost}")
st.write(f"**Result Time:** {time}")

if st.button("Book Test"):
    st.success(f"Test '{test_choice}' booked successfully! You will be notified once results are ready.")

st.markdown("---")

st.subheader("📄 View My Bookings")
st.write("- 1 Aug 2025 — CBC — ₹500")
st.write("- 29 Jul 2025 — ECG — ₹800")
