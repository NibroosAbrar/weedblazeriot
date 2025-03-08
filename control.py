import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="IoT Controller", layout="wide")

st.markdown(
    """
    <style>
    .stButton>button {
        border-radius: 50%;
        width: 80px;
        height: 80px;
        font-size: 30px;
    }
    .button-container, .control-panel {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .camera-container img {
        width: 100%;
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("WEEDBLAZER")

# Layout Setup
col_wheel, col_camera, col_manipulator = st.columns([1, 2, 1])

# Wheel Control (Left)
with col_wheel:
    st.subheader("🚗 Wheel Control")
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    if st.button("⬆️", key="wheel_up"):
        st.write("Moving Forward")
    row1, row2 = st.columns(2)
    with row1:
        if st.button("⬅️", key="wheel_left"):
            st.write("Turning Left")
    with row2:
        if st.button("➡️", key="wheel_right"):
            st.write("Turning Right")
    if st.button("⬇️", key="wheel_down"):
        st.write("Moving Backward")
    st.markdown('</div>', unsafe_allow_html=True)

# Real-Time Camera (Center)
# Real-Time Camera (Center)
with col_camera:
    st.subheader("📷 Live Camera Feed")

    # Gunakan 0 jika hanya ada satu kamera, atau ubah jika perlu
    cap = cv2.VideoCapture(-1)  
    if not cap.isOpened():
        st.error("Camera not found. Try using another index (0, 1, -1).")
    else:
        frame_placeholder = st.empty()
        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture image.")
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame, use_column_width=True, output_format="JPEG")
        cap.release()

    
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("🔥", key="laser_fire"):
        st.write("Laser Activated!")
    st.markdown('</div>', unsafe_allow_html=True)

# Cartesian Manipulator Control (Right)
with col_manipulator:
    st.subheader("🤖 Manipulator Control")
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    if st.button("⬆️", key="manip_up"):
        st.write("Moving Up")
    row3, row4 = st.columns(2)
    with row3:
        if st.button("⬅️", key="manip_left"):
            st.write("Moving Left")
    with row4:
        if st.button("➡️", key="manip_right"):
            st.write("Moving Right")
    if st.button("⬇️", key="manip_down"):
        st.write("Moving Down")
    st.markdown('</div>', unsafe_allow_html=True)

st.info("For now, Arduino communication is disabled.")

# Arduino Code (Commented Out)
"""
#include <ArduinoBLE.h>

void setup() {
    Serial.begin(9600);
    if (!BLE.begin()) {
        Serial.println("Starting BLE failed!");
        while (1);
    }
    Serial.println("BLE Ready");
}

void loop() {
    // Placeholder for Bluetooth communication with Streamlit
}
"""
