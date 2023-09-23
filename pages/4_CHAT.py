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

openai.api_key = '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'

# elastic setting
cloud_id = 'Demo_v4:YXAtbm9ydGhlYXN0LTIuYXdzLmVsYXN0aWMtY2xvdWQuY29tJGI2OTlmYzE2NWM1NzQ0YmQ4MjBjYWU5NTM0MTM3YjFiJGQ1YzIzNjViNTNjMTQwYzk5YjUyMGE2YTZkNWE2ZGQ5'
username = 'luck4'
password = '000000'
index_name='ottogi_review_v1'


es = Elasticsearch(
    cloud_id=cloud_id,
    basic_auth=(username, password),
)



### ---- langchain ---- ###


st.set_page_config(page_title="💬Chat with the Food" , page_icon="💬", layout="centered", initial_sidebar_state="auto", menu_items=None)
# openai.api_key = st.secrets.openai_key
## hide
# openai.api_key = st.secrets["openapi_key"]
##

st.title("Chat with the Ottogi 💬")

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Ottogi"}
    ]



@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading our Data – hang tight! This should take 1-2 minutes."):
        
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on ottogi companies food products and reviews"))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index
        
if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    
    
    ###----- gpt ----###
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": ""}
    ]
    
    # 대화를 통한 모델 요청
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    # 모델 응답 출력
    gpt_result = response.choices[0].message['content']
    gpt_result = gpt_result.replace(",", " ")    
    print(gpt_result)



    ### ----- langchain ---- ###
    query = {
      "query": {
        "query_string": {
          "query": f"{prompt}*"
        }
      }
    }

    
    response = es.search(index=index_name, body=query, size =50)
    
    # 검색 결과를 JSON 형태로 변환
    search_results = []
    for hit in response['hits']['hits']:
        # print(hit)
        search_results.append(hit['_source']['review'])
        
    print(search_results)
    print("length", len(search_results))
        
    with open('./data/output.txt', 'r', encoding='utf-8') as file:
        original_content = file.read()
    
    # 파일을 쓰기 모드로 엽니다.
    with open("./data/output.txt", "w", encoding="utf-8") as file:
        # 각 문자열을 파일에 작성합니다.
        for line in search_results:
            file.write(line + "\n")  # 각 줄 끝에 개행 문자("\n")를 추가합니다.
    
    print("텍스트 파일이 생성되었습니다.")
    
    index = load_data()
    chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True) 
    

    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            
            response = chat_engine.chat(prompt)
            st.write(f"{response.response} \n\n {gpt_result}")
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
            
            
            
