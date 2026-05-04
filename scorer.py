def calculate_score(resume, job_desc):

    resume_words = set(resume.lower().split())
    job_words = set(job_desc.lower().split())

    if len(job_words) == 0:
        return 0, []

    match = resume_words.intersection(job_words)

    score = len(match) / len(job_words) * 100

    return round(score, 2), list(match)