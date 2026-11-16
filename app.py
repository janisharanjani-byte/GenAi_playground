import os   
import tempfile
import base64

import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama

# =================================
# PAGE CONFIG
# =================================

st.set_page_config(
    page_title="GenAI Career Mentor",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 GenAI Career Mentor")
st.write(
    "Upload your resume and get personalized GenAI learning recommendations."
)

# =================================
# LOAD VECTOR DB
# =================================

@st.cache_resource
def load_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    return db


db = load_db()

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

# =================================
# LLM
# =================================

llm = ChatOllama(
    model="llama3",
    temperature=0
)

# =================================
# SKILL MATRIX
# =================================

required_skills = {
    "Python",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Transformers",
    "Prompt Engineering",
    "RAG",
    "Vector Database",
    "LangChain",
    "LangGraph",
    "Docker",
    "AWS",
    "Git",
    "LLM"
}

# =================================
# PDF MAPPING
# =================================

pdf_mapping = {
    "Python": r"E:\LMS AI carrer mentor\Learning materials\Python.pdf",
    "Machine Learning": r"E:\LMS AI carrer mentor\Learning materials\Machine Learning.pdf",
    "Deep Learning": r"E:\LMS AI carrer mentor\Learning materials\Deep learning.pdf",
    "NLP": r"E:\LMS AI carrer mentor\Learning materials\NLP.pdf",
    "RAG": r"E:\LMS AI carrer mentor\Learning materials\RAG End-to-End Student Handout.pdf",
    "LangChain": r"e:\LMS AI carrer mentor\Learning materials\Langchain.pdf",
    "LangGraph": r"E:\LMS AI carrer mentor\Learning materials\Langgraph.pdf",
    "Docker": r"E:\LMS AI carrer mentor\Learning materials\Docker.pdf",
    "AWS": r"E:\LMS AI carrer mentor\Learning materials\AWS.pdf",
    "Prompt Engineering": r"E:\LMS AI carrer mentor\Learning materials\prompt engineering.pdf",
    "Vector Database": r"E:\LMS AI carrer mentor\Learning materials\vector DB.pdf",
    "Transformers" : r"E:\LMS AI carrer mentor\Learning materials\transformers.pdf"
}

# =================================
# RESUME UPLOAD
# =================================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    with st.spinner("Reading Resume..."):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())

            resume_path = tmp.name

        loader = PyPDFLoader(resume_path)

        docs = loader.load()

        resume_text = "\n".join(
            [doc.page_content for doc in docs]
        )

    # =============================
    # SKILL EXTRACTION
    # =============================

    found_skills = []

    for skill in required_skills:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

    missing_skills = list(
        required_skills - set(found_skills)
    )

    # =============================
    # SCORE
    # =============================

    score = (
        len(found_skills)
        / len(required_skills)
    ) * 100

    st.metric(
        "GenAI Readiness Score",
        f"{score:.2f}%"
    )

    # =============================
    # DISPLAY SKILLS
    # =============================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Existing Skills")

        if found_skills:

            for skill in sorted(found_skills):

                st.success(skill)

        else:

            st.info("No matching skills detected")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in sorted(missing_skills):

                st.warning(skill)

        else:

            st.success(
                "All required skills found!"
            )

    # =============================
    # LEARNING RESOURCES
    # =============================

    st.subheader("📚 Recommended Learning Materials")

    for skill in sorted(missing_skills):

        pdf_path = pdf_mapping.get(skill)

        st.markdown(f"### {skill}")

        if pdf_path and os.path.exists(pdf_path):

            with st.expander(f"📘 View {skill} Notes"):
                
                st.pdf(pdf_path, height=700)    


        else:

            st.info(
                f"No PDF available for {skill}"
            )

    # =============================
    # RAG NOTES
    # =============================

    st.subheader("📖 Personalized Notes")

    for skill in sorted(missing_skills):

        docs = retriever.invoke(skill)

        context = "\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        st.markdown(
            f"## {skill}"
        )

        st.write(
            context[:1500]
        )

    # =============================
    # ROADMAP
    # =============================

    with st.spinner(
        "Generating roadmap..."
    ):

        prompt = f"""
        You are a Senior GenAI Mentor.

        Existing Skills:
        {found_skills}

        Missing Skills:
        {missing_skills}

        Create:

        1. Current profile assessment
        2. Skill gap analysis
        3. 8 week learning roadmap
        4. Capstone project ideas
        5. Interview preparation plan
        6. ATS improvement suggestions

        Keep output professional.
        """

        response = llm.invoke(
            prompt
        )

    st.subheader(
        "🎯 Personalized Career Roadmap"
    )

    st.markdown(
        response.content
    )