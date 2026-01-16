from transformers import pipeline


class EmotionEngine:
    """
    EmotionEngine is responsible for detecting emotion from text.
    It wraps a pretrained transformer model and provides a clean interface.
    """

    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            return_all_scores=True
        )

        # Define the emotions we care about (controlled set)
        self.supported_emotions = {
            "joy": "joy",
            "sadness": "sadness",
            "anger": "anger",
            "fear": "fear",
            "love": "love",
            "surprise": "surprise",
            "neutral": "neutral"
        }

    def detect_emotion(self, text):
        """
        Takes a string input and returns:
        - normalized emotion label
        - confidence score
        """

        if not text or not text.strip():
            return "neutral", 1.0

        results = self.classifier(text)[0]
        top_emotion = max(results, key=lambda x: x['score'])

        raw_label = top_emotion["label"].lower()
        score = top_emotion["score"]

        normalized_emotion = self._normalize_emotion(raw_label)

        return normalized_emotion, score

    def _normalize_emotion(self, raw_label):
        """
        Maps raw model labels to supported emotion set.
        """

        if raw_label in self.supported_emotions:
            return self.supported_emotions[raw_label]

        # Fallback
        return "neutral"
    def get_all_emotion_scores(self, text):
        """
        Returns full emotion distribution for debugging/analysis.
        """
        results = self.classifier(text)[0]
        return {item["label"]: item["score"] for item in results}
