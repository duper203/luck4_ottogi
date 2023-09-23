import json
import requests
import streamlit as st
import time
import elasticsearch


st.title("💨 Visualizing Ottogi's Review Data")
st.info("Are you curious about Evlalutaitons on Ottogi Food?\n\n"
         "We have created a dedicated webpage that beautifully visualizes Ottogi's REVIEWs, making it easier for you to explore people’s evaluation.\n\n"
         "**Also you are an administrator at Ottogi, these dashboards would enable you to quickly grasp how consumers think about Ottogi’s Food!😄**", icon="💡")

# 바로 이동할 수 있도록 6가지 항목들 링크 걸어주기 

# 1. Evaluation Stars for Ottogi
st.subheader("🌐 How Many Stars for Ottogi")
st.markdown("This dashboard offers an insightful view into the ratings that consumers have generously provided for Ottogi's diverse range of food products. To embark on a more comprehensive and interactive exploration, kindly follow the link provided below:\n\n <a href='https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs'>🔗 Click here to explore further.</a>", unsafe_allow_html=True)

# 이미지 파일 경로
image_path = './img/review_2.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Evaluation Stars for Ottogi', use_column_width=True)



# 5. 지역별 상품 판매량 (1/2)
st.subheader("🌐 Examine the distribution of ratings")
st.markdown("This service is a powerful tool designed to provide you with comprehensive insights into the distribution of ratings of products.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs)")

col1, col2 = st.columns(2)
with col1:
         # 이미지 파일 경로
         image_path = './img/review_5.jpeg' 
         # 이미지를 화면에 표시
         st.image(image_path, caption='Rate Distribution', use_column_width=True)
with col2:
         st.markdown("📍**Improved Decision Making:** By understanding how products are rated, you can make more informed decisions about which products to promote, improve, or discontinue based on customer feedback.\n\n📍 **Enhanced Product Quality:** Analyzing rating distributions can highlight areas where product quality may need improvement, leading to better overall customer satisfaction.")



# 3. USA Sales Revenue Visualization Dashboard
st.subheader("🌐 Average rating over the past 10 days")
st.markdown("This dashboard provides with average Star Rates by tracking the recent 10 days of ratings. \n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs)")

# 이미지 파일 경로
image_path = './img/review_4.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Recent Average Rate', use_column_width=True)


# 4. 판매수익이 높은 상품 상위 5개
st.subheader("🌐 Star Rates for every MONTH")
st.markdown("This dashboard provides with average Star Rates by tracking, every Month for several Years.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs)")

# 이미지 파일 경로
image_path = './img/review_7.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Average Rating for each Month.', use_column_width=True)


# 5. 지역별 상품 판매량 (1/2)
st.subheader("🌐 **Top 10** items by rating & **Bottom 10** items by rating")
st.markdown("This dashboard proviedes you with the top items of high ratings and the lowest ratings. This interactive dashboard allows you to explore and understand on products that many consumers are satisfied with and also products they were less happy with.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs)")

col1, col2 = st.columns(2)
with col1:
         # 이미지 파일 경로
         image_path = './img/review_10.jpeg' 
         # 이미지를 화면에 표시
         st.image(image_path, caption='Top 10 Ottogi Products by Rating', use_column_width=True)
with col2:
         # 이미지 파일 경로
         image_path = './img/review_11.jpeg' 
         # 이미지를 화면에 표시
         st.image(image_path, caption='Bottom 10 Ottogi Products by Rating', use_column_width=True)
         # st.markdown("📍 **Product Category Analysis**: Explore sales data categorized by product type. Understand which products are thriving in specific regions and leverage this information for targeted marketing strategies.\n\n📍 **Real-Time Data** : Our service is powered by real-time data, ensuring that you're always up-to-date with the latest Amazon sales revenue figures for Ottogi products. ")

# # 6. 지역별 인기상품 비율
# st.subheader("🌐 Bottom 10 items by rating")
# st.markdown("This dashboard also proviedes you with the items with the lowest ratings. This interactive dashboard allows you to explore and understand on products that many consumers are less satisfied with.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs)")

# col1, col2 = st.columns(2)
# with col1:
#          # 이미지 파일 경로
#          image_path = './img/review_11.jpeg' 
#          # 이미지를 화면에 표시
#          st.image(image_path, caption='Top 5 Ottogi Products by Amazon Sales Revenue with Percentage Visualization', use_column_width=True)
# with col2:
#          st.markdown("📍 **Product Category Analysis**: Explore sales data categorized by product type. Understand which products are thriving in specific regions and leverage this information for targeted marketing strategies.\n\n📍 **Real-Time Data** : Our service is powered by real-time data, ensuring that you're always up-to-date with the latest Amazon sales revenue figures for Ottogi products. ")

# 2. USA Sales Revenue Visualization Dashboard
st.subheader("🌐 What recent reviews have we received")
st.markdown("This dashboard visualizes the recent reviews consumers have posted. You can check the recent evalations right away. For a deeper and more interactive exploration, simply click on the link below:\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/rNJLs)")

# 이미지 파일 경로
image_path = './img/review_6.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Recent Review Posts', use_column_width=True)


# 7. 결론 및 기대효과 
st.subheader("📒 Conclusion and Expected Impact")
col1, col2 = st.columns(2)
with col1:
         st.info("From a CONSUMER's STANDPOINT ")
         st.markdown("✅**Quality Assurance:** A consistent high rating across products indicates that a brand or manufacturer is dedicated to maintaining product quality. Consumers can trust such brands and expect consistently good experiences. \n\n✅ **Be Informed Purchasing Decisions:** Consumers can make more informed choices by reviewing product ratings and reviews. They can easily identify high-rated products that are likely to meet their expectations, which can save time and money.")
with col2:
         st.info("From a PRODUCT MANAGER's STANDPOINT ")
         st.markdown("✅**Competitive Analysis:** By comparing their product's ratings to those of competitors, product managers can gain insights into their market position. This analysis can help identify opportunities for differentiation and competitive advantage. \n\n✅ **Product Iteration:** Ratings data can inform the product development roadmap. Product managers can identify specific areas where improvements or new features are needed to address customer concerns or enhance the product's value")