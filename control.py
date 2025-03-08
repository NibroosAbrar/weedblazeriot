import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="IoT Controller", layout="wide")

st.title("IoT Controller for Mobile")

# Layout Setup
col_wheel, col_camera, col_manipulator = st.columns([1, 2, 1])

# Wheel Control (Left)
with col_wheel:
    st.subheader("🚗 Wheel Control")
    if st.button("⬆️", use_container_width=True):
        st.write("Moving Forward")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️", use_container_width=True):
            st.write("Turning Left")
    with col2:
        if st.button("➡️", use_container_width=True):
            st.write("Turning Right")
    if st.button("⬇️", use_container_width=True):
        st.write("Moving Backward")

# Real-Time Camera (Center)
with col_camera:
    st.subheader("📷 Real-Time Camera Stream")
    camera = st.camera_input("Activate Camera")
    if camera is not None:
        st.image(camera, caption="Live Feed", use_column_width=True)

# Cartesian Manipulator Control (Right)
with col_manipulator:
    st.subheader("🤖 Manipulator Control")
    if st.button("⬆️", use_container_width=True):
        st.write("Moving Up")
    col3, col4 = st.columns(2)
    with col3:
        if st.button("⬅️", use_container_width=True):
            st.write("Moving Left")
    with col4:
        if st.button("➡️", use_container_width=True):
            st.write("Moving Right")
    if st.button("⬇️", use_container_width=True):
        st.write("Moving Down")

# Laser Control (Below Camera)
st.subheader("🔫 Laser Control")
if st.button("🔥 Fire Laser", use_container_width=True):
    st.write("Laser Activated!")

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
