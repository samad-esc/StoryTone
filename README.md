# StoryTone – Emotion-Driven AI Music Generator

StoryTone is an end-to-end AI system that converts narrative text into evolving background music by analyzing emotions and generating mood-aligned soundscapes. It combines transformer-based emotion detection with custom sound synthesis to create expressive, dynamic audio that follows the emotional journey of a story.

The project is being built with a strong emphasis on clean architecture, explainability, and product-quality engineering rather than as a toy demo.

---

## Project Status

Phase 2 – Emotion Engine & Music Engine (In Progress)

Core pipeline, emotion detection, and sound generation are functional. Refinement of sound design, transitions, and UI experience is ongoing.

---

## Vision

To build a clean, explainable, and creative AI product that blends storytelling and music through emotion-aware sound generation.

The goal is to design StoryTone as a modular, extensible system that demonstrates strong engineering discipline and creative application of AI, suitable for real-world use and technical evaluation.

---

## Overview

Stories naturally carry emotional progression, but background music is often static and disconnected from the narrative. StoryTone addresses this gap by dynamically generating music that follows the emotional flow of a story in real time.

The system processes a story sentence by sentence, detects the dominant emotion at each stage, and generates corresponding audio segments that are stitched together into a continuous soundtrack. The result is an evolving musical experience that mirrors the emotional arc of the story.

---

## Key Features

- Transformer-based emotion detection from text  
- Emotion-specific sound generation using custom audio synthesis  
- End-to-end story-to-music pipeline  
- Modular system design with clear separation of concerns  
- Interactive web interface for real-time use  
- Downloadable audio output in WAV format  

---

## System Architecture

The system is designed as a clean, modular pipeline:

User Input (Story)  
→ Emotion Engine (NLP)  
→ Emotion to Music Mapping  
→ Music Engine (Sound Synthesis)  
→ Audio Stitching Pipeline  
→ Final Soundtrack Output  

Each component is isolated for clarity, maintainability, and ease of debugging.

---

## Emotion Engine

The emotion engine is built using a pretrained transformer-based NLP model. It analyzes each sentence of the story and returns the dominant emotion along with a confidence score.

To maintain predictable system behavior, raw model outputs are normalized into a controlled set of supported emotions.

Supported emotions:
- Joy  
- Sadness  
- Anger  
- Fear  
- Love  
- Surprise  
- Neutral  

This controlled mapping makes the emotion layer reliable, explainable, and easy to extend.

---

## Music Engine

The music engine generates ambient, chord-based soundscapes based on the detected emotion. Instead of using random or pre-recorded audio, sound is synthesized programmatically to allow full control over mood and texture.

The engine incorporates:
- emotion-specific frequency mapping  
- harmonic chord structures  
- smooth fade-in and fade-out  
- slow amplitude modulation for movement  
- emotion-based texture shaping  

The focus is on expressive and intentional sound design rather than complex musical composition.

---

## Pipeline Orchestration

The pipeline coordinates the complete system flow:

1. Split the story into sentences  
2. Detect emotion for each sentence  
3. Generate emotion-based audio segment  
4. Append segments in sequence  
5. Export the final combined soundtrack  

This orchestration layer is designed to be easy to debug, easy to extend, and easy to explain in technical discussions.

---

## Web Interface

The application includes a clean, minimal web interface built using Streamlit.

Users can:
- paste a story  
- generate an emotional soundtrack  
- listen to the output in the browser  
- download the generated audio file  

The UI is intentionally kept simple and product-like to focus on functionality and clarity.

---

## Tech Stack

Language: Python  
NLP: HuggingFace Transformers  
Audio Processing: NumPy, SciPy, pydub  
UI: Streamlit  
Backend Logic: Custom Pipeline Architecture  

---

## Project Structure

StoryTone/  
├── app.py  
├── pipeline.py  
├── emotion_engine.py  
├── music_engine.py  
├── test_emotion.py  
├── test_music.py  
├── test_pipeline.py  
├── assets/  
└── README.md  

---

## How to Run Locally

Clone the repository  
git clone <your-repo-url>  
cd StoryTone  

Create a virtual environment  
python -m venv venv  

Activate the environment (Windows)  
venv\Scripts\activate  

Install dependencies  
pip install -r requirements.txt  

Run the application  
streamlit run app.py  

Open in browser: http://localhost:8501

---



## Future Improvements

- Real instrument sampling  
- Genre selection and style control  
- Visual emotion timeline  
- Real-time music generation  
- Cloud deployment and scalability  

---


