import streamlit as st
import numpy as np
import pandas as pd

st.title("this is our first project using python IDE")
st.write("this is created using python streamlit")

df = pd.DataFrame({'name':['sachin','virat','klrahul','Msdhoni'],'marks':[20,40,50,60]})
st.write(df)

data = np.array([10,20,12,45,80])
st.line_chart(data)