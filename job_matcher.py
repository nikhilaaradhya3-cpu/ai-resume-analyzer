import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_job_roles(filepath="data/job_roles.csv"):
    """
    Loads the job roles and their required skills from a CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        # Ensure all required skills are lowercase for matching
        df['required_skills'] = df['required_skills'].str.lower()
        return df
    except Exception as e:
        print(f"Error loading job roles: {e}")
        return pd.DataFrame(columns=['role', 'required_skills'])

def calculate_match_scores(extracted_skills, job_roles_df):
    """
    Compares the candidate's extracted skills with the requirements of each job role.
    Uses TF-IDF and cosine similarity to calculate a match score.
    Returns a sorted list of recommended roles.
    """
    if not extracted_skills or job_roles_df.empty:
        return []

    # Convert the candidate's list of extracted skills into a single space-separated string
    candidate_skills_str = " ".join(extracted_skills)
    
    # Prepare the list of documents for TF-IDF (Job Role Skills + Candidate Skills)
    documents = job_roles_df['required_skills'].tolist()
    documents.append(candidate_skills_str)
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Convert text to TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate cosine similarity between the candidate (last row) and all job roles
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    
    # Rank roles from highest to lowest score
    recommended_roles = []
    for idx, row in job_roles_df.iterrows():
        # Convert similarity to a percentage
        match_score = round(cosine_sim[idx] * 100, 2)
        recommended_roles.append({
            "role": row['role'],
            "score": match_score,
            "required_skills": row['required_skills'].split()
        })
        
    # Sort the roles based on the match score in descending order
    recommended_roles = sorted(recommended_roles, key=lambda x: x['score'], reverse=True)
    
    return recommended_roles