import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.set_page_config(
    page_title = "인터렉티브 대시보드"
)

plt.rcParams['font.family'] = "AppleGothic"
plt.rcParams['axes.unicode_minus'] = False

file = st.file_uploader("file(csv,excel)", type=['csv', 'xls', 'xlsx'])

time.sleep(3)
data = None
if file is not None:
    ext = file.name.split('.')[-1]
    if ext == 'csv':
        data = pd.read_csv(file)
    elif 'xls' in ext:
        data = pd.read_excel(file, engine='openpyxl')

st.dataframe(data)

fig, ax = plt.subplots()
ax.bar(data['age'], data['height'])
st.pyplot(fig)

barplot = sns.barplot(x='age', y='height', data=data, ax=ax)
fig = barplot.get_figure()

st.pyplot(fig)

