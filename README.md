Here's a more polished and professional version of your README for the **Brain Tumor Detector** project:

---

# Brain Tumor Detector using YOLOv8 and Streamlit

## Overview
The **Brain Tumor Detector** is a real-time brain tumor detection system built with the YOLOv8 deep learning model and Streamlit for an interactive web interface. This application enables users to upload brain MRI scans and leverages a custom-trained YOLOv8 model to accurately detect the presence of tumors. The results are highlighted in the MRI images, providing a clear visual representation of potential tumor regions.

## Features
- **Image Upload**: Supports uploading brain MRI scans in JPG, JPEG, and PNG formats.
- **Real-time Detection**: Detects brain tumors instantly using the YOLOv8 object detection model.
- **Tumor Highlighting**: Highlights regions in the image where tumors are detected.
- **Interactive Web Interface**: Easy-to-use, web-based interface powered by Streamlit.
- **Dual Image Display**: Displays both the original MRI image and the result with tumor detection annotations.

## Tech Stack
- **YOLOv8 (Ultralytics)**: Deep learning model for real-time object detection.
- **Streamlit**: Web app framework for building interactive interfaces.
- **OpenCV & Pillow (PIL)**: Libraries for image processing and manipulation.
- **Python**: Backend logic for model inference and app integrations.

## Model Information
The detection model, `last.pt`, is a YOLOv8 model that has been trained on a curated dataset of brain MRI images. The model is fine-tuned to detect brain tumors with high precision, enabling fast and accurate identification of abnormal regions in MRI scans.

## How to Run

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Atharva1399/brain-tumor-detector.git
cd brain-tumor-detector
```

### 2. Install Dependencies
Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
Start the Streamlit application:
```bash
streamlit run app.py
```

This will launch the web app in your default browser, where you can upload MRI scans for real-time tumor detection.

## Conclusion
The Brain Tumor Detector is an easy-to-use, high-accuracy application designed to aid in the early detection of brain tumors. By utilizing YOLOv8 for real-time object detection and Streamlit for an interactive user interface, the system provides a seamless and efficient experience for healthcare professionals and researchers alike.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---



