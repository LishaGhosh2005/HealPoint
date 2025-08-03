# pages/2_Login.py
import streamlit as st

st.set_page_config(page_title="Login - HealPoint", page_icon="🔐")
st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email and password:
        st.success("Login successful! Redirecting...")
        # You can redirect based on role in real app
    else:
        st.error("Please enter both email and password")
