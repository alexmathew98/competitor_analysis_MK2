import streamlit as st
from main import FinancialCrew  # Import the FinancialCrew class from main.py
import os

st.title('Your Research Assistant')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter Research Details')
    topic = st.text_input("Which competitor do you want to analyse:")

if st.button('Run Research'):
    if not topic:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Competition Company: {topic}\n"
        research_crew = FinancialCrew(inputs)
        result = research_crew.run()
        st.subheader("Results of your research project:")
        st.write(result)