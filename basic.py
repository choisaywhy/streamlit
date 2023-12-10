import streamlit as st

st.set_page_config(
    page_title = "기본 동작"
)
st.title('타이틀')
st.header('헤더')
st.subheader('서브헤더')
st.caption('캡션')

st.code('''
        def function():
            print('hello, world')
        ''', language="python")

st.text('텍스트')
st.markdown('마크다운 **마크다운**')
agree = st.checkbox('check?')
if agree:
    st.write('checked')

radio = st.radio(
    'select',
    ('1', '2', '3'))

if radio == '1':
    st.write('1 selected')
elif radio == '2':
    st.write('2 selected')
elif radio == '3':
    st.write('3 selected')

selectbox = st.selectbox(
    'selectbox',
    ('1', '2', '3'), 
    index=2
)

if selectbox == '1':
    st.write('1 selected')
elif selectbox == '2':
    st.write('2 selected')
elif selectbox == '3':
    st.write('3 selected')

multi_select = st.multiselect('multi selectbox',
                                ['A', 'B', 'C', 'D'])
	
st.write(multi_select,'selected:')

values = st.slider(
    '범위 지정',
    0.0, 100.0, (25.0, 75.0))
st.write(values,'selected')

text = st.text_input(
    label='insert text', 
    placeholder=''
)
st.write(f'what you wrote is {text}')

