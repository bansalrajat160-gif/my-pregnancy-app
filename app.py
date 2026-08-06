from datetime import date
import streamlit as st
from google import genai

# Page Config
st.set_page_config(page_title="Pregnancy Care AI", page_icon="👶")

st.title("✨ GEMINI ANALYSIS & Recommend")
st.write("Enter your details below to get pregnancy analysis.")

# 1. Inputs
api_key = st.text_input("Enter your Gemini API key:", type="password")
user_date = st.text_input(
    "Enter your lmp date (DD/MM/YYYY):", placeholder="e.g. 10/04/2026"
)

current_date = date.today().strftime("%d/%m/%Y")

# 2. Analyze Button
if st.button("Analyze Pregnancy"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not user_date:
        st.error("Please enter your LMP date.")
    else:
        try:
            # Official Google GenAI Client
            client = genai.Client(api_key=api_key)

            # Prompt containing ALL 10 original tasks
            prompt = f"""
You have to calculate pregnancy duration from user input date to till current date.

Task:
you have to perform all below task on the basis of pregnancy time like you have to calculate current month of pregnancy according to the lmp date which user enter.
write user's input date as lmp date and {current_date} as reports on.

1. Give pregnancy time in months.
2. Give the size of baby.
3. Give what can baby do inside.
4. Recommend diet chart to mother.
5. Give all information in grammatically correct with correct spelling and in good format.
6. Write always "बेटी बचाओ - बेटी पढ़ाओ" at last.
7. Do not give * in output.
8. Give all information only for user's current month of pregnancy
9. Give edd as well.
10. Please check if gap between user input date and {current_date} is more than 41 week then give error message type "Please enter valid lmp." And gave same error for any future date as lmp.

Input Date:
{user_date}
"""

            with st.spinner("⏳ Analyzing your Pregnancy..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash", contents=prompt
                )

            st.markdown("---")
            st.write(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
