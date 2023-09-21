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

def ocr_connect(image_file):
    api_url = '----- naver api url -----'
    secret_key = '----- naver secret key ------'
    
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
      ('file', open(image_file,'rb'))
    ]
    headers = {
      'X-OCR-SECRET': secret_key
    }
    
    response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
    
    # print(response.text.encode('utf8'))
    
    
    if response.status_code == 200:
        result = response.json()
        if 'images' in result:
            for image_info in result['images']:
                if 'fields' in image_info:
                    for field in image_info['fields']:
                        # print(f"{field['inferText']}")
                        keyword_list.append(field['inferText'])
        
        
        else:
            print("이미지 정보를 찾을 수 없습니다.")
        
        print("한장씩 keyword_list 출력완료")
        
        return keyword_list
        
        
    else:
        print(f"API 요청 실패: {response.status_code}")
        print(response.text)
    
if picture:
    ##OCR
    st.image(picture)
    img = Image.open(picture)
    button = st.button("ocr")
    
   
    
    if button:
        ocr_pic = convert_image(img)
        st.write(ocr_pic)



    ##다운로드 파일
    # st.image(picture)
    # image = Image.open(picture)
    # st.download_button("Download fixed image", convert_image(image), "fixed.png", "image/png")
