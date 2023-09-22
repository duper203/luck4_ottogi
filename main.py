import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import requests
import uuid
import time
import tempfile 
import json



# Define your Streamlit secrets here
# api_url = st.secrets["naver_api_url"]
# secret_key = st.secrets["naver_secret_key"]

def ocr_connect(image_file):
    api_url = st.secrets["naver_api_url"]
    secret_key = st.secrets["naver_secret_key"]
    
    keyword_list = []
    
    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo'
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }
    
    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [
      ('file',open(image_file,'rb'))
    ]
    headers = {
      'X-OCR-SECRET': secret_key
    }
    
    
    response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
    
    
    if response.status_code == 200:
        result = response.json()
        if 'images' in result:
            for image_info in result['images']:
                if 'fields' in image_info:
                    for field in image_info['fields']:
                        print(f"{field['inferText']}")
                        keyword_list.append(field['inferText'])
        else:
            print("이미지 정보를 찾을 수 없습니다.")
    else:
        print(f"API 요청 실패: {response.status_code}")
        print(response.text)
    
    return keyword_list
        

st.title("OCR using Naver API")
image_file = st.file_uploader("이미지 업로드", type=['png', 'jpg', 'jpeg'])

if image_file:
    print("image_file:",image_file)
    if st.button("OCR 실행"):
        
        # Create a temporary file to save the uploaded image
        with tempfile.NamedTemporaryFile(delete=False) as temp_image:
            temp_image.write(image_file.read())
            temp_image_path = temp_image.name
            ocr_text = ocr_connect(temp_image_path)

            
            
            
        
        # output_image = image_file.read()
        
        
        # # Convert the image to PNG format
        # output_image = Image.open(image_file)
        # output_image = image.convert("JPG")
        # print("image:", output_image)
        
        # ocr_text = ocr_connect(output_image)
        
        if ocr_text:
            st.write("OCR 결과:")
            for keyword in ocr_text:
                st.write(keyword)
