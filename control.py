import streamlit as st
import asyncio
from bleak import BleakClient

# UUID yang sama dengan di Arduino
SERVICE_UUID = "19B10010-E8F2-537E-4F6C-D104768A1214"
CHARACTERISTIC_UUID = "19B10011-E8F2-537E-4F6C-D104768A1214"

# Alamat perangkat Arduino (ubah sesuai perangkat)
DEVICE_ADDRESS = "4b:1b:5c:be:9d:21"

# Fungsi untuk mengecek koneksi ke Arduino
async def check_connection():
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            return await client.is_connected()
    except:
        return False

# Fungsi untuk mengirim perintah ke Arduino
async def send_command(command):
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            if await client.is_connected():
                await client.write_gatt_char(CHARACTERISTIC_UUID, command.encode())
                st.toast(f"✅ Perintah '{command}' terkirim!", icon="✅")
            else:
                st.toast("❌ Gagal terhubung ke Arduino!", icon="❌")
    except Exception as e:
        st.toast(f"⚠️ Error: {str(e)}", icon="⚠️")

# Cek koneksi saat halaman dimuat
if "is_connected" not in st.session_state:
    st.session_state.is_connected = asyncio.run(check_connection())

st.set_page_config(page_title="IoT Controller", layout="centered")

st.markdown(
    """
    <style>
    .indicator {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    .connected { background-color: #4CAF50; color: white; }
    .disconnected { background-color: #FF5733; color: white; }
    .stButton>button {
        width: 100px;
        height: 100px;
        font-size: 24px;
        margin: 10px;
        border-radius: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 IoT Mobile Controller")

# Indikator Koneksi Bluetooth
status_text = "🔗 Terhubung ke Arduino" if st.session_state.is_connected else "❌ Tidak Terhubung"
status_class = "connected" if st.session_state.is_connected else "disconnected"
st.markdown(f'<div class="indicator {status_class}">{status_text}</div>', unsafe_allow_html=True)

# Layout
st.subheader("🎮 Kontrol Pergerakan")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬆️", key="wheel_up"): asyncio.run(send_command("FORWARD"))
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️", key="wheel_left"): asyncio.run(send_command("LEFT"))
with col3:
    if st.button("➡️", key="wheel_right"): asyncio.run(send_command("RIGHT"))
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬇️", key="wheel_down"): asyncio.run(send_command("BACKWARD"))

st.subheader("🔦 Laser Control")
if st.button("🔥 Nyalakan Laser", key="laser_fire"):
    asyncio.run(send_command("LASER_ON"))

st.subheader("🤖 Kontrol Manipulator")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬆️", key="manip_up"): asyncio.run(send_command("MANIP_UP"))
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️", key="manip_left"): asyncio.run(send_command("MANIP_LEFT"))
with col3:
    if st.button("➡️", key="manip_right"): asyncio.run(send_command("MANIP_RIGHT"))
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬇️", key="manip_down"): asyncio.run(send_command("MANIP_DOWN"))

st.info("💡 Gunakan mode layar penuh untuk pengalaman terbaik di Android.")
