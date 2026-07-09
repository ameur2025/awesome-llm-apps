import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Theme Rouge
st.set_page_config(page_title="🔴 خبير العقار", page_icon="🔴", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #1a0000; }
h1 { color: #ff0000; }
.stButton>button { background-color: #ff0000; color: white; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🔴 خبير العقار المغربي بالذكاء الاصطناعي")
st.subheader("بالتعاون مع Gemini")

city = st.selectbox("📍 المدينة", ["الدار البيضاء", "مراكش", "الرباط", "طنجة", "فاس", "أكادير"])
q = st.text_area("❓ سؤالك", "مثال: شحال ثمن شقة 80 متر فمراكش")

if st.button("🔍 حلل ليا"):
    with st.spinner("كنقلب ليك..."):
        model = genai.GenerativeModel('gemini-1.5-flash')
        res = model.generate_content(f"أنت خبير عقاري مغربي. المدينة: {city}. السؤال: {q}. جاوب بالدارجة المغربية وأعطي أثمنة تقريبية")
        st.success(res.text)
