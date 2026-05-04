from parser import load_file
from scorer import calculate_score
from llm_service import analyze_resume

print("📄 AI ATS Resume Screening System")

resume_path = input("Enter resume file path: ")
job_path = input("Enter job description file path: ")

resume = load_file(resume_path)
job_desc = load_file(job_path)

score, matched = calculate_score(resume, job_desc)

analysis = analyze_resume(resume, job_desc)

print(f"\n📊 Match Score: {score}%")
print(f"\n✅ Matched Keywords:\n{matched}")

print("\n🤖 AI Analysis:\n")
print(analysis)