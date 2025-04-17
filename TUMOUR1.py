import streamlit as st
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO
import tempfile

# Load YOLOv8 model
model = YOLO("last.pt")  # Change if needed

# Streamlit page config
st.set_page_config(page_title="YOLOv8 Detection", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    html, body {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 45px;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #0072ff, #00c6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #444;
        margin-bottom: 30px;
    }
    .upload-box {
        border-radius: 20px;
        padding: 25px;
        background: rgba(255, 255, 255, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        margin-bottom: 30px;
    }
    .image-container {
        padding: 15px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<div class="title">YOLOv8 Object Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and detect objects with real-time computer vision</div>', unsafe_allow_html=True)

# Upload section
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📁 Upload Image (JPG, PNG)", type=["jpg", "jpeg", "png"])
st.markdown('</div>', unsafe_allow_html=True)

# If image is uploaded
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(image, caption="📷 Uploaded Image", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Save image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image.save(tmp.name)
        tmp_path = tmp.name

    # Run YOLOv8 detection
    results = model(tmp_path)[0]
    result_image = results.plot()  # numpy array

    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(result_image, caption="✅ Detected Objects", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
