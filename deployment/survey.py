import streamlit as st
import numpy as np
import pickle

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
            position: fixed;
            right: 0;
            left: auto;
        }
        .css-1kyxreq { /* Main content block */
            direction: rtl;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

questions = [
    "😀 أنا محور الانتباه في الحفلات.",
    "💬 ما أتكلم كثير.",
    "🤗 أشعر بالراحة حول الناس.",
    "🕶️ أفضل البقاء في الخلفية.",
    "💬 أبدأ المحادثات.",
    "🤐 ما عندي الكثير لأقوله.",
    "👥 أتكلم مع ناس مختلفين في الحفلات.",
    "🫥 ما أحب لفت الانتباه لنفسي.",
    "🌟 ما أمانع أن أكون محور الاهتمام.",
    "🤐 أكون هادئ حول الغرباء.",
    "😰 أتوتر بسهولة.",
    "🧘‍♂️ أنا مسترخي أغلب الوقت.",
    "😟 أقلق بشأن الأمور.",
    "🙂 نادرًا ما أشعر بالكآبة.",
    "😖 أكون حساس تجاه الأمور.",
    "😡 أتوتر بسرعة.",
    "🎭 مزاجي يتغير كثير.",
    "🌪️ عندي تقلبات مزاجية متكررة.",
    "😠 أكون سريع الغضب.",
    "😔 أشعر بالكآبة غالبًا.",
    "😶 ما أشعر بالكثير تجاه الآخرين.",
    "🤗 أهتم بالناس.",
    "🗣️ أسيء للناس.",
    "🤝 أتعاطف مع مشاعر الآخرين.",
    "🙅‍♂️ ما أهتم بمشاكل الآخرين.",
    "💓 عندي قلب رقيق.",
    "🛑 ما أكون مهتم بالناس.",
    "⏳ أخصص وقت للآخرين.",
    "🫂 أشعر بمشاعر الآخرين.",
    "😌 أجعل الناس يشعرون بالراحة.",
    "🗂️ دائمًا مستعد.",
    "📦 أترك أغراضي مبعثرة.",
    "🔍 أركز على التفاصيل.",
    "🧹 أفشل في ترتيب الأمور.",
    "🚀 أنجز المهام على الفور.",
    "🗂️ أنسى إعادة الأشياء إلى مكانها.",
    "📚 أحب النظام.",
    "🛌 أتهرب من مسؤولياتي.",
    "📅 ألتزم بجدولي.",
    "🎯 أكون دقيقًا في عملي.",
    "📖 عندي مفردات غنية.",
    "🧠 أجد صعوبة في فهم الأفكار المجردة.",
    "🌈 عندي خيال حي.",
    "💭 ما أهتم بالأفكار المجردة.",
    "💡 عندي أفكار رائعة.",
    "🛑 ما عندي خيال واسع.",
    "⚡ أفهم الأمور بسرعة.",
    "📝 أستخدم كلمات معقدة.",
    "🤔 أقضي الوقت في التفكير بالأشياء.",
    "🎨 أكون مليء بالأفكار."
]

options = [
    "أعترض بقوة",
    "أعترض",
    "محايد",
    "أوافق",
    "أوافق بقوة"
]
# these were inferred from the clusters (anaylized muliple rows)
cluster_descriptions = {
    0: "يا سلام، شكلك تحب الانفتاح والتعبير عن نفسك، مع لمسة من الحساسية والتفكير الإبداعي. تحب التفاصيل الدقيقة وتتميز بالالتزام، رغم أنك تميل أحيانًا للتوتر.\n\n"
       "لو بعطيك نصيحة... حاول توظيف حساسيتك وانفتاحك في مجالات تقدر فيها الابتكار والتنظيم! 🎨📋",
    1: "واضح إنك شخص اجتماعي ومغامر! عندك قدرة على الحفاظ على هدوئك حتى في أصعب الظروف، ومع ذلك تحب تكون في وسط الأحداث وتستمتع باستكشاف أشياء جديدة.\n\n"
       "لو بعطيك نصيحة... استفد من قدرتك على التأقلم وجرّب أدوار تتطلب الشجاعة والانفتاح على الآخرين! 🌍🗣️",
    2: "شخصيتك متوازنة وعملية، مع لمسة من الاستقرار العاطفي. تحب تبني أفكار جديدة، وتتصرف بتفكير وهدوء. الناس يثقون فيك لأنك متوازن ومرن.\n\n"
       "لو بعطيك نصيحة... استغل توازنك لتكون قائدًا يعتمد عليه في المواقف المختلفة! 🏗️🤝",
    3: "أنت شخص منظم وعملي جدًا، تحب إنجاز المهام بدقة وتهتم بالتفاصيل. ومع ذلك، تملك جانبًا اجتماعيًا يجعل الناس ينجذبون إليك.\n\n"
       "لو بعطيك نصيحة... استخدم طاقتك للقيادة وتنظيم المشاريع! 💼🎯",
    4: "شخصيتك تميل للتفكير والتحليل، مع بعض التردد في الانخراط الاجتماعي. حساسيتك العالية تعكس عمق تفكيرك وحرصك.\n\n"
       "لو بعطيك نصيحة... حاول تفتح نفسك أكثر للناس وكن جريئًا في التعبير عن آرائك! 🧠💬",
    5: "يا سلام! أنت شخص متوازن جدًا. عندك القليل من كل شيء، وهذا يخليك تتأقلم مع أي بيئة بسهولة. تحب تبقي الأمور سلسة وبسيطة.\n\n"
       "لو بعطيك نصيحة... استغل مرونتك في بناء علاقات قوية ومستمرة! 🤝🌟",
    6: "واضح إنك شخص حساس ومتعاطف، ومع ذلك منظم وموثوق. تعمل بشكل رائع مع الآخرين وتقدر أهمية التعاون.\n\n"
       "لو بعطيك نصيحة... حافظ على التوازن بين العمل الجماعي واهتمامك بنفسك! 🌸🛠️",
    7: "شخصيتك غامضة ومختلفة، تميل لعدم الانخراط بسهولة. قد تكون ملاحظًا أو تحب البقاء بعيدًا عن الأضواء.\n\n"
       "لو بعطيك نصيحة... افتح المجال لاستكشاف ذاتك أكثر، قد تكتشف جوانب مدهشة! 🌌🔍",
    8: "شخصيتك تجمع بين الإبداع والالتزام. تحب التفكير بطرق جديدة وتقدر النظام في الوقت نفسه. يمكن الاعتماد عليك في الابتكار والتطوير.\n\n"
       "لو بعطيك نصيحة... جرّب تحويل أفكارك الإبداعية إلى مشاريع ملموسة! ✨💡"
}


# Initialize session state
if "responses" not in st.session_state:
    st.session_state.responses = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# Sidebar
with st.sidebar:
    st.markdown(
        """
        هذا الاختبار التفاعلي يقيم سمات شخصيتك بناءً على:
        -  Extroversion 
        -  Agreeableness 
        -  Conscientiousness 
        -  Neuroticism 
        -  Openness 
        
        جاوب بصدق علشان تعرف نمط شخصيتك!
        """
    )

current_index = st.session_state.current_question
total_questions = len(questions)

if current_index < total_questions:
    # Progress bar
    st.progress(current_index / total_questions)

    # Current question
    st.subheader(questions[current_index])

    # Display buttons in rows
    for i, option in enumerate(options, start=1):
        if st.button(option, key=f"option_{current_index}_{i}"):
            st.session_state.responses.append(i)  # Save the response
            st.session_state.current_question += 1  # Move to the next question
else:
    st.header("نتائج شخصيتك")
    st.success("🎉 كملت الاختبار!")

    features = np.array(st.session_state.responses).reshape(1, -1)

    try:
        with open('big5_cluster_model.pkl', 'rb') as file:
            model = pickle.load(file)

        prediction = model.predict(features)

        st.write(f"🎉 تمت معالجة إجاباتك بنجاح! 🚀")
        st.write(f"{cluster_descriptions[prediction[0]]}")

    except Exception as e:
        st.error(f"خطأ أثناء تحميل أو استخدام النموذج: {e}")

    if st.button("إعادة الاختبار"):
        st.session_state.responses = []
        st.session_state.current_question = 0


