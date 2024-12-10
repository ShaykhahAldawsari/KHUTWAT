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

# Updated list of questions
questions = [
    "😀 أرتاح لما أكون حول الناس.",
    "💬 أبدأ المحادثات.",
    "😰 أتوتر بسهولة.",
    "🎭 مزاجي يتغير كثير.",
    "🤗 أحس بمشاعر غيري وأتعاطف معهم.",
    "⏳ أخصص وقت للناس.",
    "🔍 أدقق في التفاصيل.",
    "📅 ألتزم بجدولي.",
    "💡 أفهم الأمور بسرعة.",
    "🧘‍♂️ أفكر وأتأمل في الأشياء كثير."
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
    0: "يا سلام، شكلك تحب الهدوء والراحة بعيد عن الزحمة. تحب ترتب أمورك بعناية وكل شيء عندك بمكانه. يمكن تقضي وقتك تتأمل أو تركز على تفاصيل دقيقة مثل الرسم أو القراءة. إذا أحد قال عنك إنك منظم وعملي، أكيد بيكون صادق!\n\n"
       " لو بعطيك نصيحة...  استمتع بوقتك الهادئ، بس لا تنسى تكسر الروتين وتجرب شيء جديد بين فترة وفترة! 🎨",
    1: "واضح إنك شخص هادئ وحساس تجاه اللي حولك، لكن بنفس الوقت تحب تساعد الكل وما تقصر. يمكن أصدقاؤك يلقون فيك الشخص اللي يسمع لهم دائمًا. تحب الأفكار الجديدة وكل شيء عندك بخطة مرتبة. بس ترا ما يمنع تكافئ نفسك برحلة أو كوفي لطيف!\n\n"
       " لو بعطيك نصيحة...  حاول تعطي نفسك الأولوية بين كل هالاهتمام بالناس. أنت تستاهل الراحة مثلهم! ☕",
    2: "أوه، واضح إنك روح الجلسة! تحب تضحك وتونس اللي حولك، ودائمًا مستعد لتجربة شيء جديد. يمكن ما تحب تدقق في التفاصيل، بس تعوضها بشخصيتك الاجتماعية وحبك للاستكشاف. إذا قالوا عنك مغامر، ما كذبوا!\n\n"
       " لو بعطيك نصيحة...  لا تنسى تخطط شوي لمغامراتك، علشان كل شيء يكون ممتع بدون توتر! 🗺️",
    3: "أنت شخص حساس وحبوب، والناس حولك يحبون لطفك. بنفس الوقت تحب النظام وما تخطي خطوة إلا وأنت متأكد منها. يمكن عندك شوية انفتاح على الأفكار الجديدة، بس ما تترك راحتك لأي شيء. تحب كل شيء يكون مرتب ومريح لعقلك وقلبك.\n\n"
       " لو بعطيك نصيحة...  حاول تكون أكثر جرأة وتجرب أشياء جديدة، يمكن تكتشف شغف جديد! 🌟",
    4: "واااو، أنت ملك الاجتماعات والجلسات. تحب تجمع الناس حولك وتكون مركز الاهتمام، ومع ذلك ثابت وموزون عاطفيًا. تحب تستكشف الأماكن الجديدة وتتعلم عن كل شيء، ومعروف عنك إنك منظم ومحبوب. لو كنت مدير، أكيد فريقك بيعشقك!\n\n"
       " لو بعطيك نصيحة...  حافظ على توازنك، وخذ وقتك للاسترخاء بعيد عن الأضواء أحيانًا! 💆‍♂️",
    5: "أنت شخص مرح وحبوب، حياتك مليانة ضحك ومواقف ممتعة. يمكن ما تحب الالتزام التام بالنظام، بس تعوضها بطاقتك الإيجابية وحبك للتجارب الجديدة. الناس يحبون يكونون معك لأنك دايم تضيف جو ممتع وفكاهي.\n\n"
       " لو بعطيك نصيحة...  حاول تضيف شوية تنظيم ليومك، علشان تستمتع أكثر وما تضيع وقتك! 📅",
    6: "شخصيتك هادية ومنطوية شوي، ويمكن تحب تقضي وقتك بروحك بعيد عن الزحمة. عندك شغف تجاه الأشياء اللي تحبها، وغالبًا تكون مهتم بالتفاصيل الدقيقة. يمكن الناس يشوفونك مباشر وما تحب اللف والدوران، وهذا شي جميل!\n\n"
       " لو بعطيك نصيحة...  افتح الباب شوي للناس، يمكن تكتشف صداقات ممتعة ما كنت تتوقعها! 🤝",
    7: "واااو، واضح إنك شخص اجتماعي وتحب تتواصل مع الناس. عندك جانب حساس بس بنفس الوقت متفهم ومحبوب. الناس يثقون فيك ويحبون يستشيرونك لأنك تعرف كيف تتعامل مع المواقف. شكلك تميل للأفكار الجديدة وتحب تساعد الكل.\n\n"
       " لو بعطيك نصيحة...  خذ وقت لنفسك بعيد عن المساعدة، لأنك تستاهل تهتم بنفسك زي ما تهتم بالآخرين! 🌸",
    8: "شخصيتك تجمع كل شيء جميل! اجتماعي جدًا، حساس، ومتعاون. تحب النظام وكل شيء عندك بمكانه، ومع ذلك ما تترك فرصة لاكتشاف أفكار جديدة وتجارب ممتعة. إذا قالوا عنك إنك قائد بالفطرة، صدقهم!\n\n"
       " لو بعطيك نصيحة...  لا تنسى توازن بين شغفك وحبك للقيادة، وخذ وقت تستمتع فيه بنفسك! 🏖️"
}




if "responses" not in st.session_state:
    st.session_state.responses = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# Sidebar
with st.sidebar:
     st.markdown(
        """
        هذا الاختبار التفاعلي يقيم سمات شخصيتك بناءً على النموذج:
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
    st.success(" كملت الأختبار 🎉!")

    features = np.array(st.session_state.responses).reshape(1, -1)

    try:
        with open('mini_big5_cluster_model_scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        with open('mini_big5_cluster_model.pkl', 'rb') as file:
            model = pickle.load(file)

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)

        st.write(" تمت معالجة إجاباتك بنجاح! 🚀")
        st.write(f" {cluster_descriptions[prediction[0]]} ")

    except Exception as e:
        st.error(f"خطأ أثناء تحميل أو استخدام النموذج: {e}")

    if st.button("إعادة الاختبار"):
        st.session_state.responses = []
        st.session_state.current_question = 0
