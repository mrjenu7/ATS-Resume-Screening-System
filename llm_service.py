import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = ""

def analyze_resume(resume, job_desc):

    prompt = f"""
You are an ATS system.

Resume:
{resume}

Job Description:
{job_desc}

Provide:
1. Strengths
2. Missing skills
3. Improvement suggestions

Be clear and professional.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    return result["choices"][0]["message"]["content"]