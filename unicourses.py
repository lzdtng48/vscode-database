import streamlit as st
import pandas as pd


readcsv = ('courses.csv')

readcsv = pd.read_csv('loancsv.csv')
menu = st.sidebar.selectbox('Menu',['Register for Course','Course Database'])

if menu == 'Register for Course':
    avc = 0
    st.header('University Courses Signup')

    name = st.text_input("Input Student's Name")
    gpa = st.number_input('Input GPA',0,4)
    courses = st.number_input('Input Desired Number of Courses',0,5)

    save = st.button('Input Data')


    if save:
        if gpa >= 3.5:
            avc = 5
            st.success(f'You can register for {courses} courses')

        elif gpa >= 3.0:
            avc = 4
            st.success('You can register for up to 4 courses')
            
        elif gpa >= 2.5:
            avc = 3
            st.success('You can register for up to 3 courses')
            
        elif gpa >= 2.0:
            avc = 2
            st.success('You can register for up to 2 courses')
            
        else:
            avc = 0
            st.error('You cannot register for any courses')
            

    csvdict = {'Name':[name], 'GPA':[gpa], 'Courses':[courses], 'Available_Courses':[avc]}
    csvdf = pd.DataFrame(csvdict)

    newtable = pd.concat([readcsv,csvdf],ignore_index=True)
    newtable.to_csv('courses.csv',index=False)