import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import pytesseract

data = None
text = None


picture = st.camera_input("Take a picture")

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im
    
if picture:
    ##OCR
    st.image(picture)
    img = Image.open(picture)
    ocr_pic = convert_image(img)
    button = st.button("ocr")
    if button:
        st.write(ocr_pic)



    ##다운로드 파일
    # st.image(picture)
    # image = Image.open(picture)
    # st.download_button("Download fixed image", convert_image(image), "fixed.png", "image/png")
