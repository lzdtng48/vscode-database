import streamlit as st
import pandas as pd

readcvs = pd.read_csv('maths.csv')



st.header('Enter 2 Numbers')
n1 = int(st.number_input('1st Number'))
n2 = int(st.number_input('2nd Number'))
m = (n1 * n2)
a = (n1 + n2)
enter = st.button('Enter Numbers')

if enter:
    st.success('saved')
    result = [n1, n2, a, m]
    st.success(f"Number 1 = {n1},   Number 2= {n2},   Addition = {a},   Multiplication = {m}")
    resultdict = {'n1':[n1],'n2':[n2],'a':[a],'m':[m]}
    df = pd.DataFrame(resultdict)
    