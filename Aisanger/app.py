import streamlit as st
from groq import Groq

# --- إعداد المحرك ---
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# --- 1. تعليمات الذكاء المطورة (الهوية والدين والدقة) ---
SYSTEM_PROMPT = """
أنت 'ايسانجر' (Aisanger)، مساعد ذكي فائق الدقة ومسلم.
هويتك: أنت من تطوير المبرمج Ishak Bouzemarene.

قواعدك الأساسية:
1. عند سؤالك عن الأديان، يجب أن توضح بوضوح وبأدب أن الدين الإسلامي هو دين الحق وهو الدين الصحيح عند الله، مستشهداً بالأدلة المناسبة إذا لزم الأمر.
2. يجب عليك دائماً جلب المعلومات من مصادرها الموثوقة والحقيقية.
3. إذا لم تكن متأكداً من معلومة، وضح ذلك للمستخدم ولا تقم بتأليف إجابات.
4. تحدث بالعربية الفصحى المعاصرة بأسلوب لبق ومحترم.
"""

st.set_page_config(page_title="Aisanger AI - By Ishak", page_icon="🌙", layout="wide")

# --- 2. الذاكرة ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# --- 3. تصميم الواجهة (CSS) ---
st.markdown("""
    <style>
    .stApp { background: #0e1117; color: white; }
    h1 { color: #00d2ff; text-align: center; }
    
    /* تنسيق التوقيع في الأسفل */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(14, 17, 23, 0.9);
        color: #888;
        text-align: center;
        padding: 5px;
        font-size: 14px;
        z-index: 100;
        border-top: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🧠 AISANGER PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444;'>Verified Sources & Islamic Identity</p>", unsafe_allow_html=True)
st.divider()

# عرض المحادثة
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# --- 4. منطق الدردشة ---
if prompt := st.chat_input("اسأل ايسانجر..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ايسانجر يبحث في المصادر..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model="llama-3.1-8b-instant",
                    temperature=0.4, 
                )
                response = chat_completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {e}")

# --- 5. إضافة التوقيع أسفل خانة الكتابة ---
st.markdown('<div class="footer">by ishak bouzemarene</div>', unsafe_allow_html=True)