import streamlit as st
import pandas as pd
from resume_parser import extract_resume_text
from text_cleaner import clean_resume_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, calculate_match_scores
from roadmap_generator import analyze_skill_gap, generate_roadmap

def main():
    # Set up the Streamlit page layout
    st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
    st.title("AI Resume Analyzer & Job Recommendation System")
    st.markdown("Upload your resume to see how well it matches various job roles and discover skills you need to learn.")

    # Load datasets[cite: 1]
    skill_df = load_skill_dictionary()
    job_roles_df = load_job_roles()

    if skill_df.empty or job_roles_df.empty:
        st.error("Error loading data dictionaries. Please ensure CSV files exist in the 'data/' folder.")
        return

    # Module 1 & 7: Resume upload section and target-role selection[cite: 1]
    st.sidebar.header("Configuration")
    target_role = st.sidebar.selectbox("Select Target Role for Gap Analysis", job_roles_df['role'].tolist())
    
    uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        with st.spinner("Processing resume..."):
            # Module 2: Text Extraction and Cleaning[cite: 1]
            raw_text = extract_resume_text(uploaded_file, uploaded_file.name)
            cleaned_text = clean_resume_text(raw_text)

            # Module 3: Skill Extraction[cite: 1]
            extracted_skills = extract_skills(cleaned_text, skill_df)

        if not extracted_skills:
            st.warning("No known technical skills were found in the resume. Please check the document content.")
            return

        # Display extracted skills[cite: 1]
        st.header("Extracted Skills")
        st.write(", ".join([skill.title() for skill in extracted_skills]))

        # Module 4 & 5: Matching and Recommendation[cite: 1]
        st.header("Recommended Job Roles")
        match_results = calculate_match_scores(extracted_skills, job_roles_df)

        if match_results:
            # Recommend the top three suitable roles[cite: 1]
            top_3_roles = match_results[:3]
            
            # Create columns for displaying top 3 roles cleanly
            cols = st.columns(3)
            for i, result in enumerate(top_3_roles):
                with cols[i]:
                    st.metric(label=f"Rank {i+1}: {result['role']}", value=f"{result['score']}%")

            # Match-score chart[cite: 1]
            st.subheader("Match Score Overview")
            chart_data = pd.DataFrame(
                {"Match Score (%)": [res['score'] for res in match_results]},
                index=[res['role'] for res in match_results]
            )
            st.bar_chart(chart_data)

        # Module 6: Skill-Gap Analysis & Roadmap for Selected Target Role[cite: 1]
        st.header(f"Skill-Gap Analysis: {target_role}")
        
        # Find the specific requirements for the user's selected target role
        target_role_data = job_roles_df[job_roles_df['role'] == target_role].iloc[0]
        target_role_skills = [skill.strip() for skill in target_role_data['required_skills'].split(',')]

        found_skills, missing_skills = analyze_skill_gap(extracted_skills, target_role_skills)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Skills Found")
            for skill in found_skills:
                st.write(f"✅ {skill.title()}")
                
        with col2:
            st.subheader("Missing Skills")
            for skill in missing_skills:
                st.write(f"❌ {skill.title()}")

        # Generate a basic learning roadmap[cite: 1]
        st.subheader("Suggested Learning Roadmap")
        roadmap = generate_roadmap(missing_skills)
        for step in roadmap:
            st.info(step)
            
        # Privacy Reminder based on Responsible AI Rules[cite: 1]
        st.caption("Privacy Note: Your uploaded resume is only processed in memory and is not stored permanently.")

if __name__ == "__main__":
    main()