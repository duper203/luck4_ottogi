import streamlit as st

picture = st.camera_input("Take a picture")

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im
    
if picture:
    st.image(picture)
    image = Image.open(picture)
    st.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")
