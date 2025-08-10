from fastapi import FastAPI, UploadFile, Form, File, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, String, Float, Table, MetaData
import google.generativeai as genai
import io
from pdfminer.high_level import extract_text
import re
import traceback
import logging

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO)

# --- FastAPI Setup ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Gemini API Setup ---
genai.configure(api_key="AIzaSyArFO5d86n2kyCvdwZ9WdaBBlCywiaAbQA")  # 🔑 Replace with your actual key

# --- SQLite Setup ---
engine = create_engine("sqlite:///leaderboard.db")
metadata = MetaData()

leaderboard = Table(
    "leaderboard", metadata,
    Column("name", String, primary_key=True),
    Column("score", Float),
    Column("feedback", String),
)

metadata.create_all(engine)

# --- Resume Scoring Function ---
def score_resume_with_gemini(resume_text: str, target_role: str) -> tuple[float, str]:
    prompt = f"""
You are a resume evaluator. Score the following resume for the role '{target_role}'.
Give a score out of 100 and a brief feedback.

Resume:
{resume_text}
"""
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    content = response.text
    logging.info("Gemini response: %s", content)

    match = re.search(r"(\d{1,3})", content)
    score = float(match.group(1)) if match else 0.0
    return score, content

# --- Upload and Verify Resume ---
@app.post("/tools/verify_resume")
async def verify_resume(
    name: str = Form(...),
    target_role: str = Form(...),
    file: UploadFile = File(...),
    debug: bool = Query(False)
):
    try:
        resume_bytes = await file.read()
        resume_text = extract_text(io.BytesIO(resume_bytes))

        if not resume_text.strip():
            raise ValueError("Resume text could not be extracted. Please upload a valid PDF.")

        score, feedback = score_resume_with_gemini(resume_text, target_role)

        with engine.connect() as conn:
            conn.execute(leaderboard.insert().values(name=name, score=score, feedback=feedback))

        return {"name": name, "score": score, "feedback": feedback}

    except Exception as e:
        logging.error("Error during resume verification", exc_info=True)
        if debug:
            tb = traceback.format_exc()
            return {"error": str(e), "traceback": tb}
        raise HTTPException(status_code=500, detail=str(e))

# --- Leaderboard Endpoint ---
@app.get("/tools/leaderboard")
async def get_leaderboard():
    with engine.connect() as conn:
        result = conn.execute(leaderboard.select()).fetchall()
        sorted_entries = sorted(result, key=lambda x: x.score, reverse=True)
        return [{"name": r.name, "score": r.score, "feedback": r.feedback} for r in sorted_entries[:10]]