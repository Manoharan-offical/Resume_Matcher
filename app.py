import re
import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Resume Matcher")

resume_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
jd = st.text_area("Paste the job description here")

skills = ["python", "java", "sql", "machine learning", "data analysis",
          "html", "css", "git", "django", "flask", "pandas", "numpy",
          "aws", "excel", "power bi", "tableau", "mysql", "c++", "react",
          "communication", "teamwork", "problem solving"]

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def has_skill(skill, text):
    return re.search(r"\b" + re.escape(skill) + r"\b", text) is not None

if st.button("Match Resume with Job Description"):
    if resume_file and jd:
        resume_text = read_pdf(resume_file)
        jd_text = jd.lower()

        tfidf = TfidfVectorizer(stop_words="english")
        vectors = tfidf.fit_transform([resume_text, jd_text])
        similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]

        resume_skills = [s for s in skills if has_skill(s, resume_text)]
        jd_skills = [s for s in skills if has_skill(s, jd_text)]

        matched_skills = [s for s in jd_skills if s in resume_skills]
        missing = [s for s in jd_skills if s not in resume_skills]

        if jd_skills:
            skill_match_percentage = len(matched_skills) / len(jd_skills) * 100
        else:
            skill_match_percentage = 0

        st.metric("Skill Match", f"{skill_match_percentage:.0f}%")
        st.progress(int(skill_match_percentage))

        if skill_match_percentage >= 70:
            st.success("Strong Match")
        elif skill_match_percentage >= 40:
            st.warning("Average Match")
        else:
            st.error("Weak Match")

        st.success("Matched Skills: " + (", ".join(matched_skills) if matched_skills else "None"))
        st.error("Missing Skills: " + (", ".join(missing) if missing else "None"))
    else:
        st.warning("Please upload a resume and paste a job description.")