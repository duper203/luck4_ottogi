import streamlit as st
import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from elasticsearch import Elasticsearch
import pandas as pd
from konlpy.tag import *
from konlpy.tag import Okt

st.title("LUCK4 OTTOGI")

st.write("made by \n\n 숙명여자대학교 소프트웨어학부 김다연, 김혜수")


# 스택 설명 1
st.subheader("🚀 Our technology stack : Lambda for OCR")
st.info("When a user uploads a product image, we utilize OCR (Optical Character Recognition) to discern product information and subsequently provide relevant recipes and essential details pertaining to the product.",icon="💡")
# 이미지 파일 경로
image_path = './img/stack2.png' 
# 이미지를 화면에 표시
st.image(image_path, caption='Our technology stack : Lambda for OCR', use_column_width=True)



with st.expander("Detailed explanation of this technology stack"):
    st.write("🇰🇷 KOR")
    st.write("1. **이미지 업로드**: 사용자는 Streamlit을 통해 제품 이미지를 업로드합니다.")
    st.write("2. **OCR 처리**: Lambda는 업로드한 이미지를 OCR 기술을 사용하여 이미지에서 텍스트 정보를 추출합니다. 추출된 텍스트에는 제품명, 브랜드, 성분, 영양 정보 등이 포함됩니다.")
    st.write("3. **텍스트 분석**: 추출된 텍스트 정보는 GPT 엔진을 통해 자연어 처리 및 텍스트 분석기술을 이용하여 상품명을 반환합니다.텍스트를 토큰화하여 단어 단위로 분리하고, 제품명 및 브랜드와 같은 중요 정보를 추출합니다.")

    st.write("4. **제품 정보 검색**: 분석된 텍스트 정보를 사용하여 Elasticsearch database에 접근하여 제품에 대한 자세한 정보를 가져옵니다.")
    st.write("5. **레시피 추천**: 인식된 제품정보를 기반으로  레시피 크롤링을 진행하여 해당 제품을 사용한 요리 레시피를 추천합니다. 사용자는 업로드한 특정 제품에 맞는 다양한 레시피를 살펴볼 수 있습니다.")

    st.write("🌎 ENG")
    st.write("1. **Image Upload**: Users upload product images through Streamlit.")
    st.write("2. **OCR Processing**: Lambda utilizes OCR technology to extract text information from the uploaded images. Extracted text may include product names, brands, ingredients, nutritional information, and more.")
    st.write("3. **Text Analysis**: The extracted text information is processed using the GPT engine, employing natural language processing and text analysis techniques to return product names. The text is tokenized to break it into words, and important information such as product names and brands is extracted.")
    
    st.write("4. **Product Information Retrieval**: Using the analyzed text information, the system accesses an Elasticsearch database to retrieve detailed information about the products.")
    st.write("5. **Recipe Recommendation**: Based on the recognized product information, web scraping of recipes is performed to recommend cooking recipes that feature the recognized product. Users can explore a variety of recipes tailored to their specific uploaded products.")



# 스택 설명 2
st.subheader("🚀 Our technology stack : Lambda for ottogi recipe")
st.info("We provide users with official recipes offered by Ottogi, as well as additional recipes that can be created using the respective product by crawling the web.",icon="💡")

# 이미지 파일 경로
image_path = './img/stack1.png' 
# 이미지를 화면에 표시
st.image(image_path, caption='Our technology stack : Lambda for ottogi recipe', use_column_width=True)

with st.expander("Detailed explanation of this technology stack"):
    st.write("🇰🇷 KOR")
    st.write("1. **람다 함수를 통한 웹 스크래핑**: 사용자가 프로세스를 시작할 때마다 Lambda 함수가 호출됩니다. 이 Lambda 함수는 BeautifulSoup 웹 스크래핑 라이브러리,를 사용하여 대상 웹 사이트에서 레시피를 액세스하고 가져옵니다.")
    st.write("2. **사용자에게 레시피 전달:**: 웹 스크래핑이 완료되면 획득한 레시피가 앞선 Lambda 함수에게 반환합니다")

    st.write("🌎 ENG")
    st.write("1. **Web Scraping with Lambda Function**: A Lambda function is invoked whenever a user initiates the process. This Lambda function employs BeautifulSoup, a web scraping library, to access and retrieve recipes from target websites.")
    st.write("2. **Recipe Delivery to Users:**: After web scraping is completed, the obtained recipes are seamlessly delivered to the another lambda function.")



# Langchain & Lama Index & GPT 사용한 곳 설명
st.subheader("🚀 GEN AI THAT WE USE")
col1, col2 = st.columns(2)
with col1:
    st.info("Langchain",icon="☁️")
with col2:
    st.info("Lalma Index",icon="☁️")
# 이미지 파일 경로
image_path = './img/chatbot.png' 
# 이미지를 화면에 표시
st.image(image_path, caption='Our technology stack : Chat about Reviews', use_column_width=True)
with st.expander("Detailed explanation of this technology stack"):
    st.write("🇰🇷 KOR")
    st.write("1. **입력값에 따른 리뷰 데이터 가져오기**: 프롬프트에 사용자가 알고 싶은 리뷰를 입력 할 경우, 입력 값에 따른 리뷰들을 엘라스틱 서치에서 가져옵니다.")
    st.write("2. **람마인덱스와 챗지피티**: 해당 데이터를 바탕으로 람마인덱스와 챗지피트를 이용하여 사용자가 원하는 정보를 알려줍니다")

    st.write("🌎 ENG")
    st.write("1. **Fetch Review Data Based on Input**: When the user enters the reviews they want to know about in the prompt, we retrieve reviews based on the input from Elasticsearch.")
    st.write("2. **Lambda Index and ChatGPT**: Using this data, we use Lambda Index and ChatGPT to provide users with the information they desire.")

st.markdown("---")

# 서비스 설명1- map 시각화
st.subheader("✅ Result 1: Visualizing Ottogi's Product Data on Amazon")
st.info("We have created a dedicated webpage that **beautifully visualizes Ottogi's product information available on Amazon,** making it easier for you to explore their delicious offerings.\n\n"
         "**Also you are an administrator at Ottogi, these dashboards would enable me to quickly grasp real-time changing data trends! 😄**", icon="💡")

# 서비스 설명2- review 시각화
st.subheader("✅ Result 2: Visualizing Ottogi's Review Data")
st.info("We have created a dedicated webpage that beautifully visualizes Ottogi's REVIEWs, making it easier for you to explore people’s evaluation.Also you are an administrator at Ottogi, these dashboards would enable you to quickly grasp how consumers think about Ottogi’s Food!😄**", icon="💡")


# 서비스 설명3- ocr
st.subheader("✅ Result 3: Take a Photo and Search for the Recipe !Right Away!")
st.info("While shopping at the store, if you have any questions about a product, simply take a photo, and our service will provide you with the latest reviews and essential information 😆 마트에서 쇼핑 중 궁금한 상품이 있다면, 바로 사진을 업로드하여 최신 리뷰와 기본 정보들을 살펴보세요!", icon="💡")


# 서비스 설명4- chat
st.subheader("✅ Result 4: Chat about the product review")
st.info("Introducing a service that utilizes a GPT model generated from user reviews, allowing you to search for product feedback all in one place! 사용자들의 리뷰를 수집하여 만들어진 GPT를 활용하여,  제품 후기 정보들을 대화 형태로 검색할 수 있는 GPT서비스 입니다 :) ", icon="💡")



st.markdown("---")

# 왜 Elastic Search
st.subheader("🚀 Our technology stack : why ElasticSearch?")
col1, col2 = st.columns(2)
with col1:
     # 이미지 파일 경로
     image_path = './img/elelastic.png' 
     # 이미지를 화면에 표시
     st.image(image_path, caption='ElasticSearch', use_column_width=True)
with col2:
    st.markdown("✅ *빠른 검색 및 쿼리 처리* :  분산 검색 엔진으로, 데이터를 빠르게 색인화하고 복잡한 쿼리를 실시간으로 처리할 수 있습니다. 사용자의 검색 쿼리에 따라 적합한 상품을 빠르게 찾아줄 수 있습니다.\n\n"
    "✅ *분석 및 집계 기능* :  데이터를 분석하고 집계할 수 있는 강력한 기능을 제공합니다. 이를 통해 상품 판매 추세, 인기 상품, 사용자 검색 패턴 등을 파악하여 효과적인 추천을 구현할 수 있습니다.\n\n"
    "✅ *Machine Learning *: 사용자가 검색한 키워드 등의 정보를 활용하여 유사도를 기반으로 쿼리 결과를 제공합니다")



# 왜 Lambda
st.subheader("🚀 Our technology stack : why Lambda?")
col1, col2 = st.columns(2)
with col1:
    st.markdown("✅ *비용 효율성* :  사용한 리소스만큼만 비용을 지불하면 됩니다. 서버가 계속 실행되는 것이 아니라, 실제로 작업이 실행될 때만 비용이 발생하므로 개발 초기 비용을 절감할 수 있습니다.\n\n"
    "✅ *확장성* :  서버리스 플랫폼은 필요한 만큼의 리소스를 동적으로 할당하여 애플리케이션을 실행합니다. 이는 트래픽이나 작업 부하의 변동에 효과적으로 대응할 수 있도록 해주며, 수평 확장성을 자동으로 처리할 수 있습니다.\n\n"
    "✅ *빠른 개발 및 배포*: 서버리스 환경에서는 코드 작성부터 배포까지의 과정이 간단하며, 이를 통해 개발주기를 단축시킬 수 있습니다. ")
with col2:
     # 이미지 파일 경로
     image_path = './img/lambda.png' 
     # 이미지를 화면에 표시
     st.image(image_path, caption='ElasticSearch', use_column_width=True)




