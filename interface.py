import streamlit as st
from analysis import analyze_resume

st.set_page_config(page_title='Resume Analyzer', page_icon='📄')
st.title('Resume Analyzer using ֎🇦🇮')
st.header(' :blue[AI powered Resume analyser with given job desciption using AI 🤖🧠🇦🇮👾]')
st.subheader(''' This page helps you to compare the resume and the givne job description and provide the ATS score, probability score, goodness of fit score, skills match score, missing keywords and SWOT analysis of the resume for the given job description.''')

st.sidebar.subheader('Upload your resume here 📃')

pdf_doc = st.sidebar.file_uploader('Click here', type=['pdf'])

st.sidebar.markdown('Designed by Kirthiga R') 

st.sidebar.markdown('Git Hub : https://github.com/keerthiga2468-del/resume_analyzer.ai.git')

job_desc = st.text_area('copy paste your job description here ✒️', max_chars = 10000)

submit = st.button('Get results ')

if submit:
    with st.spinner('Loading.......⌛'):
        analyze_resume(pdf_doc, job_desc)