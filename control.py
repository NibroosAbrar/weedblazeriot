import streamlit as st
import asyncio
from bleak import BleakClient
import cv2
import numpy as np

# UUID yang sama dengan di Arduino
SERVICE_UUID = "19B10010-E8F2-537E-4F6C-D104768A1214"
CHARACTERISTIC_UUID = "19B10011-E8F2-537E-4F6C-D104768A1214"

# Alamat perangkat Arduino (ubah sesuai dengan perangkat)
DEVICE_ADDRESS = "42:48:3c:66:0c:7b"  # Ganti dengan alamat MAC Arduino Nano 33 BLE

# Fungsi untuk mengirim data ke Arduino
async def send_command(command):
    async with BleakClient(DEVICE_ADDRESS) as client:
        if await client.is_connected():
            await client.write_gatt_char(CHARACTERISTIC_UUID, command.encode())
            st.success(f"Perintah '{command}' terkirim!")
        else:
            st.error("Gagal terhubung ke Arduino!")

st.set_page_config(page_title="IoT Controller", layout="wide")

st.markdown(
    """
    <style>
    .main {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .stButton>button {
        border-radius: 50%;
        width: 80px;
        height: 80px;
        font-size: 30px;
        margin: 15px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin: 20px 0;
    }
    .section-title {
        text-align: center;
        width: 100%;
        margin-bottom: 20px;
    }
    div.element-container {
        text-align: center;
    }
    div.stButton {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("IoT Controller for Mobile")

# Layout Setup - Adjusted ratios for better proportions
col_left, col_center, col_right = st.columns([1.2, 2, 1.2])

# Wheel Control (Left)
with col_left:
    st.subheader("🚗 Wheel Control")
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬆️", key="wheel_up"):
        st.write("Moving Forward")
    st.markdown('</div>', unsafe_allow_html=True)
    
    row1, row2 = st.columns(2)
    with row1:
        if st.button("⬅️", key="wheel_left"):
            st.write("Turning Left")
    with row2:
        if st.button("➡️", key="wheel_right"):
            st.write("Turning Right")
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬇️", key="wheel_down"):
        st.write("Moving Backward")
    st.markdown('</div>', unsafe_allow_html=True)

# Real-Time Camera (Center)
with col_center:
    st.subheader("📷 Live Camera Feed")
    camera = st.camera_input("Activate Camera")
    if camera is not None:
        st.image(camera, caption="Live Feed", use_column_width=True)
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("🔥", key="laser_fire"):
        st.write("Laser Activated!")
    st.markdown('</div>', unsafe_allow_html=True)

# Cartesian Manipulator Control (Right)
with col_right:
    st.subheader("🤖 Manipulator Control")
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬆️", key="manip_up"):
        st.write("Moving Up")
    st.markdown('</div>', unsafe_allow_html=True)
    
    row3, row4 = st.columns(2)
    with row3:
        if st.button("⬅️", key="manip_left"):
            st.write("Moving Left")
    with row4:
        if st.button("➡️", key="manip_right"):
            st.write("Moving Right")
    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬇️", key="manip_down"):
        st.write("Moving Down")
    st.markdown('</div>', unsafe_allow_html=True)

st.info("For now, Arduino communication is disabled.")

st.markdown('</div>', unsafe_allow_html=True)
