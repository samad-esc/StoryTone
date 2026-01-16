from music_engine import MusicEngine

engine = MusicEngine()

emotions = ["joy", "sadness", "anger", "fear", "love", "surprise", "neutral"]

for emotion in emotions:
    file_path = engine.generate_music(emotion)
    print(f"Generated music for {emotion}: {file_path}")
