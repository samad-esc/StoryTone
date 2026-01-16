from emotion_engine import EmotionEngine
from music_engine import MusicEngine
from pydub import AudioSegment
import os


class StoryPipeline:
    """
    Orchestrates the full flow:
    Story -> Emotion detection -> Music generation -> Audio stitching
    """

    def __init__(self):
        self.emotion_engine = EmotionEngine()
        self.music_engine = MusicEngine()

    def process_story(self, story_text):
        """
        Takes full story text and returns path to final stitched audio file.
        """

        # 1. Split story into sentences
        parts = self._split_story(story_text)

        final_audio = AudioSegment.silent(duration=0)

        for idx, part in enumerate(parts):
            if not part.strip():
                continue

            # 2. Detect emotion
            emotion, score = self.emotion_engine.detect_emotion(part)
            print(f"[Pipeline] Sentence {idx+1} Emotion: {emotion} ({round(score, 2)})")

            # 3. Generate music for this emotion
            audio_file = self.music_engine.generate_music(emotion)

            # 4. Load audio and append
            segment = AudioSegment.from_wav(audio_file)
            final_audio += segment

        # 5. Export final combined audio
        output_file = "final_storytone.wav"
        final_audio.export(output_file, format="wav")

        return output_file

    def _split_story(self, story_text):
        """
        Splits story into sentences.
        """
        parts = story_text.split(".")
        return parts
