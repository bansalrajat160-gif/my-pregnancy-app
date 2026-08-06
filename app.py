import streamlit as st
from google import genai

st.title("✨ GEMINI ANALYSIS & Recommend")
st.write("Enter your details below to get pregnancy analysis.")

api_key = st.text_input("Enter your Gemini API key:", type="password")
lmp_date = st.text_input("Enter your lmp date (DD/MM/YYYY):", placeholder="29/12/2025")

if st.button("Analyze Pregnancy"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not lmp_date:
        st.error("Please enter your LMP date.")
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"Analyze pregnancy for LMP date: {lmp_date}"
            
            with st.spinner("Gemini is analyzing your Pregnancy..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt
                )
                st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
