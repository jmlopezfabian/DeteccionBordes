import streamlit as st
import cv2
import numpy as np
from pyspark.sql import SparkSession


st.title("Procesamiento Paralelo para la Detección de Bordes en Imágenes Binarias usando PySpark, OpenCV y Shiny")


st.title("Sube una imagen")
uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(img, caption="Imagen cargada", use_column_width=True)
