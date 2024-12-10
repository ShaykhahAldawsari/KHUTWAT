import streamlit as st
import os


st.markdown(
    """
    <style>
        body {
            direction: rtl;
            text-align: right;
        }
        .css-1d391kg { /* Sidebar */
            direction: rtl;
            text-align: right;
        }
        .css-1kyxreq { /* Main content block */
            direction: rtl;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(" 🧠 Big Five Personality Test")
st.markdown("🔹 **اختر النسخة اللي تناسبك من القائمة على اليمين:**")

with st.sidebar:
    st.title("📋 القائمة")
    option = st.selectbox(
        "",
        ["الصفحة الرئيسية", "📜 (50 Qs) النسخة الكاملة", "📋 (10 Qs) النسخة المصغرة"]
    )

if option == "الصفحة الرئيسية":
    st.info(" هلا والله! اختر النسخة اللي تناسبك من القائمة على اليمين علشان تبدأ الاختبار 💡")
    st.markdown(
        """
        ### تعليمات:
        1. اختر النسخة المصغرة إذا كنت تفضل اختبار سريع (10 أسئلة).
        2. اختر النسخة الكاملة إذا كنت تريد تحليلًا شاملاً (50 سؤال).
        3. الإجابات الصادقة هي اللي بتعطيك نتائج دقيقة وتحلل شخصيتك صح.
        4. ولا تنسى تضغط مرتين علشان تنتقل للسؤال التالي!
        """
    )

elif option == "📋 (10 Qs) النسخة المصغرة":
    st.info("👍🎯 تم اختيار النسخة المصغرة! ")
    exec(open("deployment/survey_mini.py", encoding="utf-8").read())

elif option == "📜 (50 Qs) النسخة الكاملة":
    st.info("👍📚 تم اختيار النسخة الكاملة!")
    exec(open("deployment/survey.py", encoding="utf-8").read())