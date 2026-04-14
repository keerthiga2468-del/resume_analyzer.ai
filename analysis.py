import os

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai 

from pdf import extract_text    # method to extract text from pdf.py file

key = os.getenv("GOOGLE_API_KEY")  # Ensure the API key is set in the environment

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite') 


def analyze_resume(pdf_doc, job_desc):
    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc)
        st.write("Text Extracted successfully ✅")
        
    else:
        st.warning('Error !! Drop the file in PDF format ')
   
    ats_score = model.generate_content(f'''Compare the given pdf {pdf_text} and given job describtion
    {job_desc} and provide ATS score on scale of 0 to 100. 
    Generate the the results in bullet points (maximum 5 points)''')
    
    probability_score = model.generate_content(f''' Compare the given pdf {pdf_text} and given job describtion
    {job_desc} and provide probability score on scale of 0 to 100.
    Generate the the results in bullet points (maximum 5 points)
    ''')
    
    goodness_of_fit_score = model.generate_content(f''' Compare the given pdf {pdf_text} and given job describtion
    {job_desc} and say whether the resume is good fit for the job describtion. If yes, provide
    the details nad if no, proide the explanation on why it is not a good fit.
    
    Generate the the results in bullet points (maximum 5 points)    
    ''')
    
    skills_match_score = model.generate_content(f''' Compare the given pdf {pdf_text} and given job describtion
    {job_desc} and give matched skills for the given job description and also giv emissing
    skills to be added in the resume for the given job description.
    
    Generate the the results in bullet points (maximum 5 points)
    ''')
    
    missing_keywords = model.generate_content(f''' Compare the given pdf {pdf_text} and given job describtion
    {job_desc} and provide the missing keywords in the resume for the given job description.
    
    Generate the the results in bullet points (maximum 5 points)
    ''')


    swot_analysis = model.generate_content(f''' Compare the given pdf {pdf_text} and given job describtion
    {job_desc} and provide SWOT analysis of the resume for the given job description. Provide the Strengths, Weaknesses, Opportunities and Threats of the resume for the given job description. 
    and also Generate the the results in bullet points (maximum 5 points)
    ''')
    
  

    return {st.write(ats_score.text),
            st.write(probability_score.text),
            st.write(goodness_of_fit_score.text),
            st.write(skills_match_score.text),
            st.write(missing_keywords.text),    
            st.write(swot_analysis.text)
            }
    