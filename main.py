import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import requests
import uuid
import time
import json

def ocr_connect(image_data):
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
        ('file', image_data)
    ]
    headers = {
        'X-OCR-SECRET': secret_key
    }
    
    response = requests.post(api_url, headers=headers, data=payload, files=files)
    
    if response.status_code == 200:
        result = response.json()
        if 'images' in result:
            for image_info in result['images']:
                if 'fields' in image_info:
                    for field in image_info['fields']:
                        keyword_list.append(field['inferText'])
        else:
            st.error("이미지 정보를 찾을 수 없습니다.")
            return
        
        st.success("OCR 완료!")
        return keyword_list
    else:
        st.error(f"API 요청 실패: {response.status_code}")
        st.error(response.text)
        return None

st.title("OCR using Naver API")
image_file = st.file_uploader("이미지 업로드", type=['png', 'jpg', 'jpeg'])

if image_file:
    print("image_file:",image_file)
    if st.button("OCR 실행"):
        # Convert the image to PNG format
        image = Image.open(image_file)
        image = image.convert("JPG")
        print("image:", image)
        
        
        ocr_text = ocr_connect(image)
        
        if ocr_text:
            st.write("OCR 결과:")
            for keyword in ocr_text:
                st.write(keyword)
