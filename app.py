import streamlit as st

st.set_page_config(page_title="Voter Eligibility Checker")

st.title("🗳️ Voter Eligibility Checker")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0)
citizen = st.radio("Are you an Indian citizen?", ("Yes", "No"))

if st.button("Check Eligibility"):
    if age >= 18 and citizen == "Yes":
        st.success(f"✅ {name}, you are eligible to vote!")
    else:
        st.error(f"❌ {name}, you are NOT eligible to vote.")
        st.info("Conditions:\n• Age must be 18+\n• Must be an Indian citizen")