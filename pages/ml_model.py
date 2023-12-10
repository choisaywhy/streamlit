import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer #sentenceBERT 모델 사용
from sklearn.metrics.pairwise import cosine_similarity
import json

st.set_page_config(
    page_title = "ML 모델 프로토타입"
)

@st.cache_resource()
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache_data()
def get_dataset():
    df = pd.read_csv('./wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('심리상담 챗봇')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# 텍스트를 입력하여 봇과 대화 할 수 있는 폼 생성
# clear_on_submit 옵션을 통해서 submit 하면 폼의 내용이 지워짐
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('당신 : ', '')
    submitted = st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input) 
    # 입력한 메시지의 유사도를 확인하여 가장 유사한 답변을 제시
    df['similarity'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[ df['similarity'].idxmax() ]

    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['챗봇'])


# 저장된 대화 내용 보여주기
for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i], key=str(i) + '_bot')