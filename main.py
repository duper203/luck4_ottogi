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
        st.write("pushed")
        text = pytesseract.image_to_string(img)
        ocr_text = st.code(text, language='text')

        st.write(ocr_text)


    ##다운로드 파일
    # st.image(picture)
    # image = Image.open(picture)
    
    # file_bytes = convert_image(image).read()
    # st.download_button("Download fixed image", convert_image(image), "fixed.png", "image/png")
