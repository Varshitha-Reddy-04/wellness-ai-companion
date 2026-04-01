from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.database import get_db
from models.schema import Log, LogResponse, LogDB, UserDB
from logic.auth_handler import get_current_user
from logic.helpers import calculate_burnout, get_suggestions, generate_insight, get_emotional_support
from logic.rule_engine import analyze_patterns
from logic.ai_analyzer import analyze_sentiment
from logic.weekly_analyzer import generate_weekly_forecast

router = APIRouter()

@router.post("/log", response_model=LogResponse)
def create_log(log: Log, db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    # Save to DB assigned to specific user
    new_entry = LogDB(
        user_id=current_user.id,
        mood=log.mood,
        sleep=log.sleep,
        work_hours=log.work_hours,
        screen_time=log.screen_time,
        journal_text=log.journal_text
    )
    db.add(new_entry)
    db.commit()

    # AI logic
    score = calculate_burnout(log)
    suggestions = get_suggestions(log)
    insight = generate_insight(log)
    support = get_emotional_support(log)

    # Pattern Detection Alerts for specific user
    alerts = analyze_patterns(db, LogDB, log, user_id=current_user.id)

    # NLP Sentiment Analysis
    sentiment_data = analyze_sentiment(log.journal_text)
    if sentiment_data["sentiment_insight"]:
        alerts.append(sentiment_data["sentiment_insight"])
    
    score += sentiment_data["score_adjustment"]
    score = max(0, min(100, score))

    return {
        "status": "success",
        "burnout_score": score,
        "insight": insight,
        "suggestions": suggestions,
        "quote": support["quote"],
        "all_quotes": support["all_quotes"],
        "music": support["music"],
        "alerts": alerts
    }

@router.get("/history")
def get_history(db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    logs = db.query(LogDB).filter(LogDB.user_id == current_user.id).all()
    return [
        {
            "mood": l.mood,
            "sleep": l.sleep,
            "work_hours": l.work_hours,
            "screen_time": l.screen_time,
            "journal_text": l.journal_text
        }
        for l in logs
    ]

@router.get("/insights/weekly")
def get_weekly_insights(db: Session = Depends(get_db), current_user: UserDB = Depends(get_current_user)):
    suggestions = generate_weekly_forecast(db, current_user.id)
    return {"weekly_suggestions": suggestions}
