import streamlit as st
import asyncio
from bleak import BleakClient

# UUID yang sama dengan di Arduino
SERVICE_UUID = "19B10010-E8F2-537E-4F6C-D104768A1214"
CHARACTERISTIC_UUID = "19B10011-E8F2-537E-4F6C-D104768A1214"

# Alamat perangkat Arduino (ubah sesuai dengan perangkat)
DEVICE_ADDRESS = "42:48:3C:66:0C:7B"

# Fungsi untuk mengecek koneksi ke Arduino
async def check_connection():
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            return await client.is_connected()
    except Exception as e:
        return False

# Fungsi untuk mengirim perintah ke Arduino
async def send_command(command):
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            if await client.is_connected():
                await client.write_gatt_char(CHARACTERISTIC_UUID, command.encode())
                st.success(f"Perintah '{command}' terkirim!")
            else:
                st.error("Gagal terhubung ke Arduino!")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Mengecek koneksi BLE saat halaman dimuat
if "is_connected" not in st.session_state:
    st.session_state.is_connected = asyncio.run(check_connection())

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
    .indicator {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 10px;
    }
    .connected {
        background-color: #4CAF50;
        color: white;
    }
    .disconnected {
        background-color: #FF5733;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("IoT Controller for Mobile")

# Indikator Koneksi Bluetooth
status_text = "🔗 Terhubung ke Arduino" if st.session_state.is_connected else "❌ Tidak Terhubung"
status_class = "connected" if st.session_state.is_connected else "disconnected"
st.markdown(f'<div class="indicator {status_class}">{status_text}</div>', unsafe_allow_html=True)

# Layout Setup
col_left, col_center, col_right = st.columns([1.2, 2, 1.2])

# Wheel Control (Left)
with col_left:
    st.subheader("🚗 Wheel Control")
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬆️", key="wheel_up"):
        asyncio.run(send_command("FORWARD"))
    st.markdown('</div>', unsafe_allow_html=True)

    row1, row2 = st.columns(2)
    with row1:
        if st.button("⬅️", key="wheel_left"):
            asyncio.run(send_command("LEFT"))
    with row2:
        if st.button("➡️", key="wheel_right"):
            asyncio.run(send_command("RIGHT"))

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬇️", key="wheel_down"):
        asyncio.run(send_command("BACKWARD"))
    st.markdown('</div>', unsafe_allow_html=True)

# Real-Time Camera (Center)
with col_center:
    st.subheader("📷 Live Camera Feed")
    camera = st.camera_input("Activate Camera")
    if camera is not None:
        st.image(camera, caption="Live Feed", use_column_width=True)
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("🔥", key="laser_fire"):
        asyncio.run(send_command("LASER_ON"))
    st.markdown('</div>', unsafe_allow_html=True)

# Cartesian Manipulator Control (Right)
with col_right:
    st.subheader("🤖 Manipulator Control")
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬆️", key="manip_up"):
        asyncio.run(send_command("MANIP_UP"))
    st.markdown('</div>', unsafe_allow_html=True)

    row3, row4 = st.columns(2)
    with row3:
        if st.button("⬅️", key="manip_left"):
            asyncio.run(send_command("MANIP_LEFT"))
    with row4:
        if st.button("➡️", key="manip_right"):
            asyncio.run(send_command("MANIP_RIGHT"))

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("⬇️", key="manip_down"):
        asyncio.run(send_command("MANIP_DOWN"))
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
