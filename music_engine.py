import numpy as np
from scipy.io.wavfile import write


class MusicEngine:
    """
    MusicEngine generates soft, ambient soundscapes based on emotion.
    """

    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

        self.emotion_frequency_map = {
            "joy": 600,
            "sadness": 220,
            "anger": 800,
            "fear": 300,
            "love": 440,
            "surprise": 700,
            "neutral": 350
        }

    def generate_music(self, emotion, duration=4):
        frequency = self.emotion_frequency_map.get(emotion, 350)

        tone = self._generate_chord(frequency, duration, emotion)
        tone = self._apply_fade(tone)

        filename = f"audio_{emotion}.wav"
        write(filename, self.sample_rate, tone.astype(np.float32))

        return filename

    def _generate_chord(self, base_freq, duration, emotion):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        if emotion == "joy" or emotion == "surprise":
            # Major chord (happy)
            freq1 = base_freq
            freq2 = base_freq * 1.25
            freq3 = base_freq * 1.5

        elif emotion == "sadness":
            # Minor chord (sad)
            freq1 = base_freq
            freq2 = base_freq * 1.2
            freq3 = base_freq * 1.5

        elif emotion == "fear":
            # Dissonant (tense)
            freq1 = base_freq
            freq2 = base_freq * 1.1
            freq3 = base_freq * 1.6

        elif emotion == "anger":
            # Strong, sharp
            freq1 = base_freq
            freq2 = base_freq * 1.3
            freq3 = base_freq * 1.7

        elif emotion == "love":
            # Warm and smooth
            freq1 = base_freq
            freq2 = base_freq * 1.25
            freq3 = base_freq * 1.4

        else:  # neutral
            freq1 = base_freq
            freq2 = base_freq * 1.2
            freq3 = base_freq * 1.4

        wave1 = np.sin(2 * np.pi * freq1 * t)
        wave2 = np.sin(2 * np.pi * freq2 * t)
        wave3 = np.sin(2 * np.pi * freq3 * t)

        chord = (wave1 + wave2 + wave3) / 3

        # Add slow volume modulation for movement
        modulator = 0.5 * (1 + np.sin(2 * np.pi * 0.3 * t))
        chord = chord * modulator

        # Emotion-specific texture adjustments
        if emotion == "sadness":
            chord = chord * 0.6  # softer, heavier feel

        elif emotion == "anger":
            chord = chord * 1.2  # stronger, aggressive

        elif emotion == "fear":
            noise = 0.02 * np.random.randn(len(chord))
            chord = chord + noise  # slight instability

        elif emotion == "love":
            chord = chord * 0.8  # gentle and smooth

        return chord



    def _apply_fade(self, wave):
        fade_length = int(0.1 * len(wave))

        fade_in = np.linspace(0, 1, fade_length)
        fade_out = np.linspace(1, 0, fade_length)

        wave[:fade_length] *= fade_in
        wave[-fade_length:] *= fade_out

        return wave
