# HealPoint Main App
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="HealPoint", page_icon="🩺", layout="centered")

# Load logo
img_path = os.path.join("assets", "healpoint_logo.png")
if os.path.exists(img_path):
    image = Image.open(img_path)
    st.image(image, use_column_width=True)

# Welcome Text
st.markdown("""
<h1 style='text-align: center; color: #1c3c6b;'>Welcome to HealPoint</h1>
<p style='text-align: center; font-size: 20px;'>Because Every Life Deserves Smart Care</p>
""", unsafe_allow_html=True)

# Action Buttons
st.markdown("""
<div style='text-align: center;'>
    <a href='/Login'><button style='padding: 10px 30px; font-size: 18px; margin: 10px; background-color: #007BFF; color: white; border: none; border-radius: 10px;'>Login</button></a>
    <a href='/Signup'><button style='padding: 10px 30px; font-size: 18px; margin: 10px; background-color: #28a745; color: white; border: none; border-radius: 10px;'>Sign Up</button></a>
    <a href='/Guest_Dashboard'><button style='padding: 10px 30px; font-size: 18px; margin: 10px; background-color: #6c757d; color: white; border: none; border-radius: 10px;'>Continue as Guest</button></a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<p style='text-align: center; font-size: 14px;'>Your digital doorway to better health.</p>
""", unsafe_allow_html=True)
