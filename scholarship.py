import streamlit as st
import pandas as pd

readcsv = ('scholarship.csv')
menu = st.sidebar.selectbox('Menu',['Check Scholarship','Scholarship Database'])

if menu == 'Check Scholarship':
    st.header('Scholarship Eligibility')
    english = st.number_input('Enter English GPA:')
    maths = st.number_input('Enter Maths GPA:')
    science = st.number_input('Enter Science GPA:')
    history = st.number_input('Enter History GPA:')
    art = st.number_input('Enter Art GPA:')
    average = (english + maths + science + history + art) / 5

    save = st.button('Save results')

    if save:
        if average >= 4.0:
            scholarship = 'Full'
        elif average >= 3.5:
            scholarship = 'Half'
        elif average >= 3.0:
            scholarship = 'Partial'
        elif average >= 2.5:
            scholarship = 'None'
        else:
            scholarship = 'None'


        csvdict = {'Name':[name], 'GPA':[average], 'Scholarship':[scholarship]}
        csvdf = pd.DataFrame(csvdict)

        newtable = pd.concat([readcsv,csvdf],ignore_index=True)
        newtable.to_csv('scholarship.csv',index=False)

elif menu == 'Scholarship Database':
    st.dataframe(readcsv)