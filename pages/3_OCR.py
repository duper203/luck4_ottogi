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
    # api_url = st.secrets["naver_api_url"]
    # secret_key = st.secrets["naver_secret_key"]
    api_url = 'https://97c3ecilit.apigw.ntruss.com/custom/v1/24213/3330ee526497f746fcd16ae438b02b1fc334fb816c12edc24d4b448753f718c3/general'
    secret_key = 'a2d2bnVzTUVrYndHZEZ0RGxBd3pHV0ZXcXlQWlFNUVg='
    
    keyword_list = ''
    
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
                        keyword_list += f"{field['inferText']} "

        
        else:
            print("이미지 정보를 찾을 수 없습니다.")
    else:
        print(f"API 요청 실패: {response.status_code}")
        print(response.text)
    
    return keyword_list
        

st.title("💨Take a Photo and Search for the Recipe !Right Away!")
image_file = st.file_uploader("이미지 업로드", type=['png', 'jpg', 'jpeg'])
ocr_keywords = ""
if image_file:
    print("image_file:",image_file)
    if st.button("Search for a Recipe"):
        
        # Create a temporary file to save the uploaded image
        with tempfile.NamedTemporaryFile(delete=False) as temp_image:
            temp_image.write(image_file.read())
            temp_image_path = temp_image.name
            ocr_text = ocr_connect(temp_image_path)

        
        if ocr_text:
            # st.write("OCR 결과:")
            
            for keyword in ocr_text:
                
                st.write(keyword)
                ocr_keywords += keyword
            
            
            headers ={
                "Content-Type": "application/json; charset=utf-8"
                
            }
        
            body = {
                "keyword": f"{ocr_keywords}"
            }
        
        
            res = requests.get(url="https://azvkqnar1c.execute-api.ap-northeast-2.amazonaws.com/default/luck4_ottogi", headers=headers, json=body)
            print(res)
            print('res.text', res.text)
            result = res.text.encode('utf-8').decode('unicode_escape')
            # st.write('result', result)
            
            res_dict = json.loads(res.text)
            
            print('res_dict', res_dict)
            st.write(res_dict)
            

            # st.write(res_dict)
            
            
            
            # st.subheader("🍽️ Recipies Available for this product")
            
            # recipe_result_dict = res_dict['recipe_result_dict']
            # i = 0
            # for key, value in recipe_result_dict.items():
            #     st.write(f"🍌 {key} \n\n 🔗 {value}")
            #     i += 1
            # st.write(res_dict['recipe_result_dict'])
            
            # st.subheader("🗂️TOP 5 REVIEWS")
            # review_dict = res_dict['search_results']

            # if len(review_dict) < 5:
            #     for reviews in review_dict:
            #         review = reviews['review']
            #         st.write(f"📍{review}")
                    
            # else:       
            #     for i in range(0, 5):
            #         reviews=review_dict[i]
            #         review = reviews['review']
            #         st.write(f"📍{review}")
            
