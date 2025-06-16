# app.py

import streamlit as st
from agent.analyzer import analyze_submissions
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LeetCode Submission Analyzer", layout="centered")

st.title("📊 LeetCode Submission Analyzer for OKRs")
st.markdown("Upload your LeetCode CSV file to get consistency and topic feedback. Powered by Gemini AI.")

# File upload section
uploaded_file = st.file_uploader("📁 Upload CSV File (submissions)", type=["csv"])

if uploaded_file is not None:
    with st.spinner("Analyzing your submission..."):
        try:
            # Save uploaded file temporarily
            file_path = os.path.join("data", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            # Analyze and display results
            result = analyze_submissions(file_path)
            st.success("✅ Analysis Complete!")
            st.markdown("### 🧠 Feedback")
            st.text(result)

        except Exception as e:
            st.error(f"❌ Error during analysis: {e}")
else:
    st.info("Please upload your submission CSV to begin.")
