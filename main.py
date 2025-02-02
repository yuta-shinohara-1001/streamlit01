import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('★Streamlit★')
st.sidebar.write('interactive')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
'Done!!'


# if st.checkbox('image'):
#     img = Image.open('xxx.png')
#     st.image(img,caption='xxx',use_container_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好き数字は、',option,'です。'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ｘｘｘｘｘ')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.sidebar.text_input('あなたの趣味を教えて')
'あなたの趣味は、',text,'です。'

condetion = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'あなたの調子は',condetion,'です。'

