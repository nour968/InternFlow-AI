
import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Project Uploader", page_icon="📤", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput>div>input {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Header with icon
st.title("📤 Upload Your Project File")
st.write("Easily send your project details and file to the server.")

# Input section
st.subheader("📝 Project Details")
project_title = st.text_input("Enter Project Title", "Web development Internship")

# File upload section
st.subheader("📂 Upload Excel File")
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

# Submit button
if st.button("🚀 Submit"):
    if uploaded_file is not None:
        with st.spinner("Uploading... Please wait"):
            data = {"project_title": project_title}
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            }
            url = "https://apprehensibly-cresylic-layla.ngrok-free.dev/process-project"

            try:
                response = requests.post(url, data=data, files=files)
                if response.status_code == 200:
                    st.success("✅ Request successful!")
                    st.json(response.json())
                else:
                    st.error(f"❌ Error: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")
    else:
        st.warning("📌 Please upload a file before submitting.")
