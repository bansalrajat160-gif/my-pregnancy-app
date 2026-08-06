from datetime import date
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Pregnancy Care AI", page_icon="👶")

st.title("✨ GEMINI ANALYSIS & Recommend")
st.write("Enter your details below to get pregnancy analysis.")

api_key = st.text_input("Enter your OpenRouter API key:", type="password")
user_date = st.text_input(
    "Enter your lmp date (DD/MM/YYYY):", placeholder="e.g. 10/04/2026"
)

current_date = date.today().strftime("%d/%m/%Y")

if st.button("Analyze Pregnancy"):
    if not api_key:
        st.error("Please enter your OpenRouter API key.")
    elif not user_date:
        st.error("Please enter your LMP date.")
    else:
        try:
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
            )

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
Input Code/Problem:
{user_date}
"""

            with st.spinner("⏳ Analyzing your Pregnancy..."):
                response = client.chat.completions.create(
                    model="meta-llama/llama-3.3-70b-instruct:free",
                    messages=[{"role": "user", "content": prompt}],
                )
                st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
