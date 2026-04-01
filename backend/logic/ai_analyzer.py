from textblob import TextBlob

def analyze_sentiment(journal_text: str) -> dict:
    """
    Analyzes the sentiment of the provided journal text.
    Returns a dictionary with sentiment polarity, subjectivity, and an insight message.
    """
    if not journal_text or len(journal_text.strip()) == 0:
        return {
            "polarity": 0.0,
            "subjectivity": 0.0,
            "sentiment_insight": None,
            "score_adjustment": 0
        }

    blob = TextBlob(journal_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    insight = None
    score_adjustment = 0

    if polarity <= -0.5:
        insight = "🗣️ AI Sentiment: Your journal entry indicates high stress or negativity today. It's okay to feel this way, but please consider resting."
        score_adjustment = 15 # Increase burnout risk
    elif polarity < 0:
        insight = "🗣️ AI Sentiment: You seem a bit down in your notes. Try doing something you enjoy!"
        score_adjustment = 5
    elif polarity > 0.5:
        insight = "🗣️ AI Sentiment: Your journal entry is highly positive! Great job maintaining a good mindset."
        score_adjustment = -10 # Decrease burnout risk
    elif polarity > 0:
        insight = "🗣️ AI Sentiment: You seem to be in a relatively positive mood based on your notes."
        score_adjustment = -5

    return {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment_insight": insight,
        "score_adjustment": score_adjustment
    }
