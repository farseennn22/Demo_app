import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LLM",
    layout="centered"
)

# Application title
st.title("AI Interview")
st.caption("Practice and Prepare for your placement")

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

# Job role selection
role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Senior Software Engineering",
        "Data Analysis",
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

# Difficulty level
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

# Generate Questions
if mode == "Generate Questions":

    count = st.slider(
        "Number of Questions",
        1, 10, 5
    )

# Generate Code Questions
elif mode == "Generate Code Questions":

    topic = st.selectbox(
        "Select Topic",
        ["Python", "C++", "C", "DSA", "Aptitude", "Java"]
    )

    count = st.slider(
        "Number of Questions",
        1, 10, 5
    )

# Evaluate or Improve Answers
else:

    question = st.text_area(
        "Enter Interview Question Here"
    )

    answer = st.text_area(
        "Enter Your Answer",
        height=160
    )

# Generate AI Response Button
if st.button("Generate AI Response", type="primary"):

    # Input validation
    if mode in ["Evaluate Answers", "Improve Answers"]:

        if not question.strip() or not answer.strip():
            st.warning("Please enter a valid Question and Answer.")
            st.stop()

    # Topics and difficulty
    topics = (
        "Job Role: " + role +
        "\nDifficulty: " + level
    )

    # Task generation
    if mode == "Generate Questions":

        task = (
            "Generate " + str(count) +
            " frequently asked interview questions for the job role "
            + role +
            ". Include 3 situation-based questions and 2 theory questions."
        )

    elif mode == "Generate Code Questions":

        task = (
            "Generate " + str(count) +
            " frequently asked coding or technical questions "
            "for the topic " + topic +
            ". Also provide hints and explain the expected approach."
        )

    elif mode == "Evaluate Answers":

        task = (
            "Question: " + question +
            "\nAnswer: " + answer +
            "\nEvaluate the answer based on the question. "
            "Identify the drawbacks, strengths, and areas of improvement."
        )

    elif mode == "Improve Answers":

        task = (
            "Question: " + question +
            "\nAnswer: " + answer +
            "\nImprove the answer and highlight the important points."
        )

    # Combine instructions
    prompt = topics + "\n" + task

    # Call Groq API
    try:

        with st.spinner("Generating AI Response..."):

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7
            )

            ai_response = response.choices[0].message.content

        # Display response
        st.subheader("AI Generated Response")
        st.write(ai_response)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
