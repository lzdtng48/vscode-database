import streamlit as st
import pandas as pd

readcsv = pd.read_csv('journal.csv')

menu = st.sidebar.selectbox('Menu',['Input Data', 'Journal'])

if menu == ('Input Data'):
    st.header('Input Data Below')
    title = st.text_input('Topic Title')
    content = st.text_input('Topic Content')
    date = st.text_input('Topic Date')
    author = st.text_input("Author's Name")

    save = st.button('Save Journal Entry')


    if save:
        st.success('Saved!')
        journaldict = {'Title':[title],'Content':[content],'Date':[date],'Author':[author]}
        journaldf = pd.DataFrame(journaldict)
        newtable = pd.concat([readcsv,journaldf],ignore_index=True)
        newtable.to_csv('journal.csv',index=False)

elif menu == ('Journal'):
    st.header('Journal Entries')
    st.table(readcsv)