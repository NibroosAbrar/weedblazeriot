import streamlit as st
import requests

FASTAPI_URL = "http://YOUR_FASTAPI_SERVER/send_command"  # Ganti dengan alamat FastAPI

def send_command(command):
    response = requests.post(FASTAPI_URL, json={"command": command})
    if response.status_code == 200:
        st.success(f"Perintah '{command}' dikirim!")
    else:
        st.error("Gagal mengirim perintah.")

st.button("Hidupkan LED", on_click=lambda: send_command("LED_ON"))
st.button("Matikan LED", on_click=lambda: send_command("LED_OFF"))
