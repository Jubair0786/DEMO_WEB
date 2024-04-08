import streamlit as st
import csv

def write_to_csv(data):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
st.title("***Welcome to Python Project***")
st.header("***Welcome to Student***")
st.subheader("Enter your data for python project:/")
U_ID = st.text_input("1.Enter Your UID")
name = st.text_input("2.Enter Your Name:")
fname = st.text_input("3.Enter Your Father Name:")
Branch = st.selectbox("4.Enter Your BranchName", ('b.tech', 'medical', 'commerce'))
classdata = st.selectbox("5.Enter Your DepartName", ('CSE', 'BBA', 'BSC', 'BA', 'MA'))
section = st.selectbox("6.Enter your SectionName", (901, 902, 903, 904, 905, 906, 908, 804, 803, 806, 704, 706, 805))
project = st.selectbox("7.Enter Your ProjectName", ('DBMS', 'PYTHON', 'OS', 'other'))
adr = st.text_area("8.Enter Your Address:")

button = st.button("Done")

if button:
    st.markdown(f"""
    UID: {U_ID}
    Name: {name}
    Father Name: {fname}
    Address: {adr}
    Branch Name: {Branch}
    DepartName: {classdata}
    SectionName: {section}
    ProjectName: {project}
    """)
    data = [U_ID, name, fname, adr, Branch, classdata, section, project]
    write_to_csv(data)