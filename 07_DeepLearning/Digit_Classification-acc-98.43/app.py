# app.py
import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image, ImageOps
import numpy as np
from streamlit_drawable_canvas import st_canvas
import cv2

# ---- Model Definition ----
class MNISTClassifier(nn.Module):
    def __init__(self):
        super(MNISTClassifier, self).__init__()
        self.flatten = nn.Flatten()
        self.net = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        return self.net(x)

# ---- Load Trained Model ----
@st.cache_resource
def load_model(path="model.pt"):
    model = MNISTClassifier()
    model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

# ---- Image Preprocessing ----
def preprocess_image(img):
    img = ImageOps.grayscale(img)
    img = img.resize((28, 28))
    img = transforms.ToTensor()(img)
    img = transforms.Normalize((0.5,), (0.5,))(img)
    return img.unsqueeze(0)

def predict_digit(img_tensor):
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
    return predicted.item()

# ---- UI Layout ----
st.set_page_config(page_title="Handwritten Digit Recognition", layout="centered")

st.title("🔢 Handwritten Digit Recognition")
st.write("Draw, upload, or capture a digit (0-9) to let the model predict.")

option = st.radio("Choose Input Method", ["🖌️ Draw Digit", "📁 Upload Image", "📷 Use Webcam"])

# ---- 1. Draw ----
if option == "🖌️ Draw Digit":
    st.subheader("Draw a digit below:")
    canvas_result = st_canvas(
        fill_color="#000000",
        stroke_width=12,
        stroke_color="#FFFFFF",
        background_color="#000000",
        width=280,
        height=280,
        drawing_mode="freedraw",
        key="canvas",
    )
    if canvas_result.image_data is not None:
        img = Image.fromarray((canvas_result.image_data[:, :, 0]).astype(np.uint8))
        if st.button("Predict"):
            input_tensor = preprocess_image(img)
            result = predict_digit(input_tensor)
            st.success(f"🧠 Model Prediction: **{result}**")

# ---- 2. Upload ----
elif option == "📁 Upload Image":
    uploaded_file = st.file_uploader("Upload a digit image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        input_tensor = preprocess_image(img)
        result = predict_digit(input_tensor)
        st.success(f"🧠 Model Prediction: **{result}**")

# ---- 3. Webcam ----
elif option == "📷 Use Webcam":
    img_file = st.camera_input("Take a photo")
    if img_file:
        img = Image.open(img_file)
        st.image(img, caption="Captured Image", use_column_width=True)
        input_tensor = preprocess_image(img)
        result = predict_digit(input_tensor)
        st.success(f"🧠 Model Prediction: **{result}**")
