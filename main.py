from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: List[str]

def analyze_sentiment(sentence: str) -> str:
    text = sentence.lower()

    positive = [
        "love", "happy", "good", "great", "excellent",
        "amazing", "wonderful", "best", "like", "enjoy",
        "awesome", "fantastic", "thank", "beautiful"
    ]

    negative = [
        "sad", "bad", "terrible", "hate", "awful",
        "worst", "angry", "disappointed", "horrible",
        "poor", "failed", "upset", "unhappy"
    ]

    pos = sum(word in text for word in positive)
    neg = sum(word in text for word in negative)

    if pos > neg:
        return "happy"
    if neg > pos:
        return "sad"
    return "neutral"

@app.post("/sentiment")
async def sentiment(request: SentimentRequest):
    return {
        "results": [
            {
                "sentence": sentence,
                "sentiment": analyze_sentiment(sentence)
            }
            for sentence in request.sentences
        ]
    }
