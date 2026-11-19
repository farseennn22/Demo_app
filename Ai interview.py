import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LLM",
    layout="centered"
)

# Application title
st.title("AI Interview")
st.caption("Practice and Prepare for your Placement")

# Import Groq safely
try:
    from groq import Groq
except ImportError:
    st.error("Groq package is not installed.")
    st.info("Add groq to your requirements.txt file and redeploy.")
    st.stop()

# API configuration
try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Streamlit Secrets.")
    st.stop()

# Success message
st.success("Groq API connected successfully!")

st.write("Welcome to your AI Interview Assistant.")

# Job title selection
role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Senior Software Engineer",
        "Data Analyst",
        "Cyber Security",
        "Software Developer",
        "Others"
    ]
)

if role == "Others":
    role = st.text_input("Enter your Job Title", "XXXXXX")

# Model selection
model = st.selectbox(
    "Choose your model",
    [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b"
    ]
)

# Experience level
level = st.selectbox(
    "Choose your level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# Activity selection
mode = st.radio(
    "Activity",
    [
        "Generate Questions",
        "Generate Code Questions",
        "Evaluate Answers",
        "Improve Answers"
    ]
)

# Generate questions
if mode == "Generate Questions":

    count = st.slider(
        "Number of Questions",
        1, 10, 5
    )

# Generate coding questions
elif mode == "Generate Code Questions":

    topic = st.selectbox(
        "Select Topic",
        [
            "Python",
            "C++",
            "C",
            "DSA",
            "Aptitude",
            "Java"
        ]
    )

    count = st.slider(
        "Number of Questions",
        1, 10, 5
    )

# Evaluate or improve answers
else:

    question = st.text_area(
        "Enter Interview Question Here"
    )

    answer = st.text_area(
        "Enter Your Answer",
        height=160
    )

    if st.button("Generate AI Response", type="primary"):

        if not question.strip() or not answer.strip():
            st.warning("Please enter a valid Question and Answer.")
            st.stop()
