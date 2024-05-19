#Create a an Arithmetic Calculator that performs addition, subtraction, division and multiplication operation between two numbers.
#Ensure to add an image if you wish and also make use of buttons ‘+’, ‘-‘, ‘/‘, and ‘*’.

import streamlit as st

st.header('Arithmetic Caluclator')

c1,c2,c3,c4,c5,c6 = st.columns(6)

with c1:
    num1 = st.number_input(' ')
with c2:
    bp = st.button('_+_')
with c3:
    bm = st.button('_-_')
with c4:
    bt = st.button('_*_')
with c5:
    bd = st.button('_/_')
with c6:
    num2 = st.number_input('  ')



if bp:
    symbol = ('+')
    ans = num1 + num2
    st.write(f'{num1}+{num2}={ans}')
if bm:
    symbol = ('-')
    ans = num1 - num2
    st.write(f'{num1}-{num2}={ans}')
if bt:
    symbol = ('*')
    ans = num1 * num2
    st.write(f'{num1}*{num2}={ans}')
if bd:
    symbol = ('/')
    ans = num1 / num2
    st.write(f'{num1}/{num2}={ans}')