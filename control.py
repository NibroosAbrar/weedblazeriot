import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.set_page_config(page_title="IoT Controller", layout="centered")

st.title("IoT Controller for Mobile")

# Control for Wheels
st.subheader("Wheel Control")
col1, col2 = st.columns(2)
with col1:
    if st.button("⬆️ Forward", use_container_width=True):
        st.write("Moving Forward")
with col2:
    if st.button("⬇️ Backward", use_container_width=True):
        st.write("Moving Backward")

# Control for Cartesian Manipulator
st.subheader("Cartesian Manipulator Control")
col3, col4, col5 = st.columns(3)
with col3:
    if st.button("⬅️ Left", use_container_width=True):
        st.write("Moving Left")
with col4:
    if st.button("⬆️ Up", use_container_width=True):
        st.write("Moving Up")
with col5:
    if st.button("➡️ Right", use_container_width=True):
        st.write("Moving Right")

col6, col7 = st.columns(2)
with col6:
    if st.button("⬇️ Down", use_container_width=True):
        st.write("Moving Down")

# Laser Control
st.subheader("Laser Control")
if st.button("🔥 Fire Laser", use_container_width=True):
    st.write("Laser Activated!")

st.subheader("Real-Time Camera Stream")

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

webrtc_streamer(key="camera", video_transformer_factory=VideoTransformer)

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