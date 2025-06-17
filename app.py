from procesamientoImagenes import ProcesamientoImagenes
import streamlit as st
import cv2
import numpy as np

st.title("Procesamiento Paralelo para la Detección de Bordes en Imágenes Binarias usando PySpark, OpenCV y Shiny")


st.subheader("Sube una imagen")
uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    # Mostrardo la imagen original
    st.subheader("Imagen Original")
    st.image(img, caption="Imagen cargada", use_column_width=True)
    procesamiento = ProcesamientoImagenes()
    st.subheader(procesamiento.prueba())
    