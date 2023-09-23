import json
import requests
import streamlit as st
import time
import elasticsearch


st.title("💨 Visualizing Ottogi's Product Data on Amazon ")
st.info("Are you curious about Ottogi, the renowned food company, and the wide array of products it offers on Amazon?\n\n"
         "Look no further! We have created a dedicated webpage that **beautifully visualizes Ottogi's product information available on Amazon,** making it easier for you to explore their delicious offerings.\n\n"
         "**Also you are an administrator at Ottogi, these dashboards would enable me to quickly grasp real-time changing data trends!😄**", icon="💡")

# 바로 이동할 수 있도록 6가지 항목들 링크 걸어주기 


# 1. USA Regional Sales Data Visualization Dashboard
st.subheader("🌐 USA Regional Sales Data Visualization Dashboard")
st.markdown("This dashboard visualizes regional sales data, offering a comprehensive view of sales across different regions of the United States. For a more detailed and dynamic exploration, click on the following link:\n\n <a href='https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/auOhO'>🔗 Click here to explore further.</a>", unsafe_allow_html=True)

# 이미지 파일 경로
image_path = './img/awsmapcount.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='USA Regional Sales Data Visualization Dashboard', use_column_width=True)



# 2. USA Sales Revenue Visualization Dashboard
st.subheader("🌐 USA Sales Revenue Visualization Dashboard")
st.markdown("This powerful tool provides an insightful view of revenue generated through product sales across various regions. For a deeper and more interactive exploration, simply click on the link below:\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/auOhO)")

# 이미지 파일 경로
image_path = './img/awsmaprevenue.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='USA Sales Revenue Visualization Dashboard', use_column_width=True)


# 3. USA Sales Revenue Visualization Dashboard
st.subheader("🌐 Sales Insights Hub: Monitoring Daily Product Sales and Visitor Traffic")
st.markdown("Dashboard Tracking Daily Visitors to the Product Sales Page and Product Quantity Trends. This dashboard offers a comprehensive view of daily visitor statistics for the product sales page on AWS and tracks trends in product quantity sold over time.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/auOhO)")

# 이미지 파일 경로
image_path = './img/awsdategraph.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Sales Insights Hub: Monitoring Daily Product Sales and Visitor Traffic', use_column_width=True)


# 4. 판매수익이 높은 상품 상위 5개
st.subheader("🌐 Top 5 Ottogi Products by Amazon Sales Revenue with Percentage Visualization")
st.markdown("This service is designed to provide you with valuable insights into Ottogi products that have achieved the highest sales revenue on Amazon. We identify the top 5 best-performing Ottogi products in terms of Amazon sales revenue and visualize the percentage of the total sales revenue they contribute.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/auOhO)")

# 이미지 파일 경로
image_path = './img/awstop5.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Top 5 Ottogi Products by Amazon Sales Revenue with Percentage Visualization', use_column_width=True)


# 5. 지역별 상품 판매량 (1/2)
st.subheader("🌐 US Regional Product Sales Visualization Dashboard")
st.markdown("This service is a powerful tool designed to provide you with comprehensive insights into product sales across different regions in the United States. This interactive dashboard allows you to explore and understand sales trends, identify regional preferences, and make data-driven decisions with ease.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/auOhO)")

col1, col2 = st.columns(2)
with col1:
         # 이미지 파일 경로
         image_path = './img/awsstatescount.jpeg' 
         # 이미지를 화면에 표시
         st.image(image_path, caption='Top 5 Ottogi Products by Amazon Sales Revenue with Percentage Visualization', use_column_width=True)
with col2:
         st.markdown("📍 **Product Category Analysis**: Explore sales data categorized by product type. Understand which products are thriving in specific regions and leverage this information for targeted marketing strategies.\n\n📍 **Real-Time Data** : Our service is powered by real-time data, ensuring that you're always up-to-date with the latest Amazon sales revenue figures for Ottogi products. ")

# 6. 지역별 인기상품 비율
st.subheader("🌐 Regional Best-Selling Products Sales Visualization Dashboard")
st.markdown("This dynamic platform is your gateway to understanding the popularity and sales performance of products in various regions. Whether you're a retailer, marketer, or simply curious about regional consumer preferences, this dashboard provides essential insights through captivating visualizations.\n\n [🔗 Click here to explore further.](https://demo-v4.kb.ap-northeast-2.aws.elastic-cloud.com:9243/app/r/s/auOhO)")

# 이미지 파일 경로
image_path = './img/awspopularproduct.jpeg' 
# 이미지를 화면에 표시
st.image(image_path, caption='Regional Best-Selling Products Sales Visualization Dashboard', use_column_width=True)


# 7. 결론 및 기대효과 
st.subheader("📒 Conclusion and Expected Impact")
col1, col2 = st.columns(2)
with col1:
         st.info("From a CONSUMER's STANDPOINT ")
         st.markdown("✅  *Informed Choices*: With access to real-time sales data and insights, you can make more informed purchasing decisions, choosing products that are popular and highly rated in your area.\n\n✅  *Better Deals* : As businesses optimize their strategies based on regional data, you may find more competitive pricing and exclusive offers on products you desire.")

with col2:
         st.info("From a PRODUCT MANAGER's STANDPOINT ")
         st.markdown("✅  *Inventory Optimization*: Businesses can better manage inventory by stocking products that are likely to sell well in specific regions, reducing overstock and waste.\n\n ✅  *Profit Maximization* : By aligning product pricing and promotions with regional demand, profitability can be significantly improved.")

