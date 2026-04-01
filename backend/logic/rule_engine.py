from sqlalchemy.orm import Session

def analyze_patterns(db: Session, LogDB, current_log, user_id: int) -> list[str]:
    """
    Analyzes historical data to detect patterns and return alerts.
    """
    alerts = []
    
    # Fetch recent history (ordered by id descending)
    # We fetch 5 entries because the current log hasn't been committed yet
    recent_logs = db.query(LogDB).filter(LogDB.user_id == user_id).order_by(LogDB.id.desc()).limit(5).all()

    # Rule 1: "Low mood streak"
    if current_log.mood <= 2:
        consecutive_low = 1
        for log in recent_logs:
            if log.mood <= 2:
                consecutive_low += 1
            else:
                break
                
        if consecutive_low >= 3:
            alerts.append("⚠️ Alert: You've had a consistently low mood for the past few entries. Please prioritize self-care or reach out to someone you trust.")

    # Rule 2: "High screen time leading to low sleep"
    if current_log.screen_time > 5 and current_log.sleep < 6:
        alerts.append("📈 Pattern detected: High screen time seems to correspond with a lack of sleep. Try a 'digital sunset' an hour before bed.")

    # Rule 3: "Overwork Streak -> Burnout Risk"
    if current_log.work_hours > 8:
        high_work_days = 1
        for log in recent_logs:
            if log.work_hours > 8:
                high_work_days += 1
            else:
                break
        
        if high_work_days >= 3:
            alerts.append("🔥 Burnout Risk: You've been logging >8 work hours for multiple entries in a row. A break is highly recommended.")

    # Rule 4: "Study hours ↑ -> stress ↑" - Simple check: if work hours are high and mood is low
    if current_log.work_hours >= 7 and current_log.mood <= 2:
        alerts.append("🔍 Insight: Your heavy workload is acutely impacting your mood today. If possible, defer some tasks.")

    return alerts
