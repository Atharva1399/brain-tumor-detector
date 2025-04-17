# brain-tumor-detector
🧠 Brain Tumor Detector using YOLOv8 and Streamlit
This project is a real-time brain tumor detection system built using YOLOv8 for object detection and Streamlit for an interactive web interface. The application allows users to upload brain MRI scans and detects the presence of tumors with high accuracy using a custom-trained deep learning model.

🔍 Features
📁 Upload MRI images (JPG, JPEG, PNG)

⚡ Real-time object detection using YOLOv8

🧠 Highlights regions with detected brain tumors

🌐 Easy-to-use web interface powered by Streamlit

📸 Displays both original and result images

🧰 Tech Stack
YOLOv8 (Ultralytics) – Deep learning model for detection

Streamlit – Web app framework

OpenCV & Pillow (PIL) – Image processing

Python – Backend logic and integrations

🚀 How to Run==>

Clone the repository:-
git clone https://github.com/Atharva1399/brain-tumor-detector.git
cd brain-tumor-detector

Install dependencies:-
pip install -r requirements.txt

Run the Streamlit app:-
streamlit run app.py

📦 Model Information
The detection model last.pt was trained using the YOLOv8 framework on a curated dataset of brain MRI images. It is fine-tuned to identify tumor regions with high precision.



