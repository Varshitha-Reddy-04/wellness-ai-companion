from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.schema import LogDB

def generate_weekly_forecast(db: Session, user_id: int):
    one_week_ago = datetime.utcnow() - timedelta(days=7)
    logs = db.query(LogDB).filter(LogDB.user_id == user_id).filter(LogDB.created_at >= one_week_ago).all()
    
    if len(logs) < 3:
        return ["Not enough data yet. Keep logging your days so I can learn your patterns!"]

    suggestions = []
    
    avg_sleep = sum(l.sleep for l in logs) / len(logs)
    avg_screen = sum(l.screen_time for l in logs) / len(logs)
    avg_work = sum(l.work_hours for l in logs) / len(logs)
    
    if avg_sleep < 6.5:
        suggestions.append("Your average sleep last week was critically low. Let's aim to go to bed 30 minutes earlier this coming week. Set a strict cutoff time.")
    
    if avg_screen > 6:
        suggestions.append("High screen time detected across the week. Try scheduling a 'no-phone' hour right after dinner to give your eyes a break.")
        
    high_work_low_mood = [l for l in logs if l.work_hours > 7 and l.mood <= 2]
    if len(high_work_low_mood) > 1:
        suggestions.append("You consistently felt stressed on days with >7 hours of work last week. Next week, try breaking your heavy work days into smaller chunks (e.g. Pomodoro technique).")
        
    low_mood_days = [l for l in logs if l.mood <= 2]
    if len(low_mood_days) >= 3:
        suggestions.append("You've had a tough week emotionally. To avoid the same mistakes next week, clear your schedule on Wednesday to decompress entirely.")
        
    if avg_work > 8:
        suggestions.append("You're continuously overworking (averaging >8hrs). Next week, try hard-stopping work at 6 PM on mid-week days to avoid burnout.")

    if not suggestions:
        suggestions.append("Your routine looks very balanced! Maintain this steady pace into next week.")

    return suggestions
