def analyze_skill_gap(extracted_skills, target_role_skills):
    """
    Compares the skills extracted from the resume with the selected role's requirements.
    Identifies which skills are present and which are missing.
    """
    # Convert lists to sets for easy comparison
    extracted_set = set(extracted_skills)
    target_set = set(target_role_skills)
    
    # Identify the overlap and the gap
    found_skills = list(extracted_set.intersection(target_set))
    missing_skills = list(target_set.difference(extracted_set))
    
    return found_skills, missing_skills

def generate_roadmap(missing_skills):
    """
    Generates a basic, rule-based learning roadmap based on the identified missing skills.
    """
    if not missing_skills:
        return ["Excellent! Your resume already contains all the core required skills for this role."]
        
    roadmap = []
    
    # Create a simple week-by-week plan for each missing skill
    for i, skill in enumerate(missing_skills):
        week_num = i + 1
        # Capitalize the skill for better presentation
        formatted_skill = skill.title()
        
        # Rule-based roadmap generation for the beginner approach
        roadmap.append(f"Week {week_num}: Focus on {formatted_skill} basics and complete a small introductory project.")
        
    return roadmap