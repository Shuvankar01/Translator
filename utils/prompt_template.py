# utils/prompt_template.py

def build_prompt_for_resume(data):
    """
    Build a clear English prompt for the Gemini model from translated data.
    `data` expected keys: name, role, experiences (str or list), skills (str/list), certs (str/list).
    """
    name = data.get("name", "")
    role = data.get("role", "")
    experiences = data.get("experiences", "")
    if isinstance(experiences, list):
        experiences = "\n".join([f"- {e}" for e in experiences])
    skills = data.get("skills", "")
    if isinstance(skills, list):
        skills = ", ".join(skills)
    certs = data.get("certs", "")
    if isinstance(certs, list):
        certs = ", ".join(certs)

    prompt = f"""
You are an expert resume writer. Create a concise, professional one-page resume in clear, professional English for the following candidate.

Name: {name}
Target role: {role}

Work experience:
{experiences}

Skills: {skills}
Certifications: {certs}

Write an output with: (1) a short professional summary (2) bullet-pointed experience items (achievements & measurable results when possible) (3) skills list. Keep it recruiter-friendly and concise.
"""
    return prompt
