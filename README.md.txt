# AI Resume Analyzer and Job Recommendation System

An NLP-based educational application built with Streamlit that helps students evaluate how well their resumes match specific job roles. The system extracts text from resumes, identifies technical skills, calculates a match score using TF-IDF and cosine similarity, and generates a personalized learning roadmap.

## Features
* **Multi-Format Support:** Upload resumes in both PDF and DOCX formats.
* **Skill Extraction:** Automatically parses and extracts technical skills while retaining important symbols (e.g., C++, C#, .NET).
* **Job Role Matching:** Compares extracted skills against industry roles like Data Analyst, ML Engineer, and AI Engineer.
* **Match Scoring:** Calculates an objective percentage score based on cosine similarity.
* **Skill-Gap Analysis:** Clearly highlights both matched and missing skills for a targeted role.
* **Learning Roadmap:** Generates a rule-based, week-by-week learning plan for missing skills.

## Technology Stack
* **Language:** Python
* **Frontend:** Streamlit
* **Text Extraction:** `pypdf`, `python-docx`
* **Data Processing & ML:** `pandas`, `numpy`, `scikit-learn`
* **Text Cleaning:** Regular Expressions (Regex)

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ai-resume-analyzer.git](https://github.com/your-username/ai-resume-analyzer.git)
   cd ai-resume-analyzer