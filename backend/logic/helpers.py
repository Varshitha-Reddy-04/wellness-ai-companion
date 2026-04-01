import random

def calculate_burnout(log):
    score = 0
    if log.mood <= 2:
        score += 30
    if log.sleep < 6:
        score += 30
    if log.work_hours > 8:
        score += 40
    return score

def get_suggestions(log):
    suggestions = []
    if log.sleep < 6:
        suggestions.append("Try sleeping earlier today 😴")
    if log.work_hours > 8:
        suggestions.append("Take short breaks during work 🧘")
    if log.mood <= 2:
        suggestions.append("Talk to someone you trust ❤️")
    if not suggestions:
        suggestions.append("You're doing great! Keep it up 👍")
    return suggestions

def generate_insight(log):
    if log.sleep < 6 and log.work_hours > 8:
        return "Your stress may be caused by high workload and lack of sleep."
    elif log.mood <= 2:
        return "Your mood has been low. Try taking some time to relax."
    else:
        return "Your routine looks balanced. Keep it up 👍"

def get_emotional_support(log):
    low = ["Tough times don’t last, but tough people do 💪", "You are stronger than you think 🌟", "Every day is a fresh start 🌅"]
    medium = ["Keep going, you’re doing great 👍", "Small progress is still progress 🚀"]
    high = ["You’re doing amazing! Keep shining ✨", "Stay positive and spread good vibes 😄"]

    if log.mood <= 2:
        return {"quote": random.choice(low), "all_quotes": low, "music": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"]}
    elif log.mood == 3:
        return {"quote": random.choice(medium), "all_quotes": medium, "music": ["https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"]}
    else:
        return {"quote": random.choice(high), "all_quotes": high, "music": []}
