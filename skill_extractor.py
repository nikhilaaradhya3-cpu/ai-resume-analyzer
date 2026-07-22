import pandas as pd
import re

def load_skill_dictionary(filepath="data/skill_dictionary.csv"):
    """
    Loads the controlled list of technical and job-related skills from a CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        # Ensure all skills are lowercase for matching
        df['skill'] = df['skill'].str.lower()
        return df
    except Exception as e:
        print(f"Error loading skill dictionary: {e}")
        return pd.DataFrame(columns=['skill', 'category'])

def extract_skills(cleaned_text, skill_df):
    """
    Searches the cleaned resume text for skills listed in the dictionary using keyword matching.
    Returns a unique list of found skills.
    """
    if cleaned_text == "" or skill_df.empty:
        return []

    found_skills = set()
    
    for skill in skill_df['skill']:
        # Use regex word boundaries to ensure we match whole words only 
        # (e.g., matching "c" won't falsely trigger on "machine")
        # For skills with special characters (like c++), we escape them in regex
        escaped_skill = re.escape(skill)
        
        # \b doesn't work well with symbols like ++ or #, so we handle them specifically
        if not skill.isalnum():
            pattern = r'(?<!\S)' + escaped_skill + r'(?!\S)'
        else:
            pattern = r'\b' + escaped_skill + r'\b'
            
        if re.search(pattern, cleaned_text):
            found_skills.add(skill)
            
    return list(found_skills)