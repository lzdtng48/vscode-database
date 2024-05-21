import streamlit as st
import pandas as pd 

readcsv = pd.read_csv('loancsv.csv')
menu = st.sidebar.selectbox('Menu',['Check Loan Eligibility','Loan Database'])

if menu == 'Check Loan Eligibility':
    st.header('Loan Eligility Checker')

    name = st.text_input('Input Name')
    income = st.number_input('Input Annual Income')
    credit_score = st.number_input('Input Credit Score')

    save = st.button('Enter')

    if save:
        if income >= 100000 and credit_score >= 800:
            loan = ('Large')
            st.success('You are eligible for a large loan.')
        elif income >= 50000 and credit_score >= 700:
            loan = ('Medium')
            st.success('You are eligible for a medium loan.')
        elif income >= 30000 and credit_score >= 600:
            loan = ('Small')
            st.success('You are eligible for a small loan.')
        else:
            st.error('You are not eligible for a loan.')
            loan = ('None')

    csvdict = {'Name':[name], 'Income':[income], 'Credit_Score':[credit_score], 'Loan':[loan]}
    csvdf = pd.DataFrame(csvdict)

    newtable = pd.concat([readcsv,csvdf],ignore_index=True)
    newtable.to_csv('loancsv.csv',index=False)

elif menu == 'Loan Database':
    st.dataframe(readcsv)
