import streamlit as st
import pandas as pd
from data_extractor import extract_financial_data

st.set_page_config(page_title="Financial Data Extractor", layout="centered")

# --- Title ---
st.title("📊 Financial Data Extractor")


# --- Input Box ---
paragraph = st.text_area("Enter financial paragraph:", height=200)

# --- Extract Button ---
if st.button("Extract"):
    if not paragraph.strip():
        st.warning("Please enter a paragraph to extract data from.")
    else:
        # Call the extraction function
        data = extract_financial_data(paragraph)

        # Build DataFrame
        df = pd.DataFrame({
            "Measure": ["Revenue", "EPS"],
            "Estimated": [data.get("revenue_expected", "N/A"), data.get("eps_expected", "N/A")],
            "Actual": [data.get("revenue_actual", "N/A"), data.get("eps_actual", "N/A")]
        })

        # Display Table
        st.subheader("📋 Extracted Financial Data")
        st.table(df)
