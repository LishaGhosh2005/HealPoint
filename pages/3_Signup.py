# pages/3_Signup.py
import streamlit as st

st.set_page_config(page_title="Signup - HealPoint", page_icon="📝")
st.title("📝 Create a New Account")

email = st.text_input("Email")
name = st.text_input("Full Name")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if email and name and password == confirm:
        st.success("Account created! Please login.")
    else:
        st.error("Please complete all fields correctly.")
