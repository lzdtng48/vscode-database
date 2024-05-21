import streamlit as st
import pandas as pd

readcsv = pd.read_csv('carsalary.csv')
st.title("Car Finder")
menu = st.sidebar.selectbox('Menu',['Buy Car', 'Car Database'])

if menu == 'Buy Car':

    st.header('Input Data Here')
    name = st.text_input('Enter Name:')
    salary = st.number_input('Input Salary: $',step=100000)

    save = st.button('Save Data')

    if save:
        st.success('Saved')
        if salary >= 200000:
            car = ('supercar')
        elif salary >= 199999:
            car = ('luxury car')
        elif salary >= 99999:
            car = ('mid-range')
        elif salary >= 59999:
            car = ('economy')
        elif salary >= 29999:
            car = ('used')
        else:
            car = ('none')

        csvdict = {'Name':[name], 'Salary':[salary], 'Car_Type':[car]}
        csvdf = pd.DataFrame(csvdict)

        newtable = pd.concat([readcsv,csvdf],ignore_index=True)
        newtable.to_csv('carsalary.csv',index=False)


elif menu == 'Car Database':
    st.table(readcsv)