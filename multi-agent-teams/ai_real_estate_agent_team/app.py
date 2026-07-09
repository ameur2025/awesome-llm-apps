import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="🏠 خبير العقار")
st.title("🏠 خبير العقار المغربي بالذكاء الاصطناعي")

city = st.selectbox("المدينة", ["الدار البيضاء", "مراكش", "الرباط", "طنجة", "فاس", "أكادير"])
q = st.text_area("سؤالك", "مثال: شحال ثمن شقة 80 متر فمراكش")

if st.button("🔍 حلل ليا"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    res = model.generate_content(f"أنت خبير عقاري مغربي. المدينة: {city}. السؤال: {q}. جاوب بالدارجة وأعطي أثمنة تقريبية")
    st.success(res.text)
