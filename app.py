import streamlit as st
import pandas as pd
from utils.ai_assistant import generate_summary

st.set_page_config(
    page_title="AI Patient Case Summarizer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Patient Case Summarizer")
st.caption("Educational AI tool for organizing patient case information")

st.divider()

# Load sample cases
cases = pd.read_csv("data/sample_cases.csv")

# Sidebar
with st.sidebar:
    st.header("📋 Sample Cases")

    selected_case = st.selectbox(
        "Choose a sample case",
        cases["case_id"]
    )

    case = cases[cases["case_id"] == selected_case].iloc[0]

    st.info(
        f"Category: {case['category']}\n\n"
        f"Symptoms: {case['symptoms']}"
    )

# Patient information
st.header("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Patient Age",
        min_value=1,
        max_value=120,
        value=20
    )

with col2:
    medical_history = st.text_area(
        "Medical History",
        placeholder="Enter relevant medical history"
    )

symptoms = st.text_area(
    "🩺 Symptoms",
    value=case["symptoms"],
    placeholder="Example: fever, cough, sore throat"
)

st.divider()

if st.button("✨ Generate AI Summary", use_container_width=True):

    if symptoms.strip():

        with st.spinner("AI is generating the summary..."):

            result = generate_summary(
                age,
                symptoms,
                medical_history
            )

        st.success("Summary generated successfully!")

        st.header("📄 AI Generated Summary")

        st.write(result)

    else:
        st.warning("Please enter the symptoms.")

st.divider()

st.caption(
    "⚠️ Educational purpose only. This tool does not provide medical diagnosis or prescribe medicines."
)