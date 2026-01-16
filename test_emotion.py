from emotion_engine import EmotionEngine

engine = EmotionEngine()

tests = [
    "She was extremely happy to see him after so many years.",
    "The room felt empty and silent.",
    "He was furious at the unfair decision.",
    "Fear crept in as the lights went out.",
    "I love the way you smile.",
    "The result was completely unexpected."
]

for text in tests:
    emotion, score = engine.detect_emotion(text)
    print(f"Text: {text}")
    print(f"Detected Emotion: {emotion} | Confidence: {round(score, 3)}")
    print("-" * 50)
