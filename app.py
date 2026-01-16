import streamlit as st
from pipeline import StoryPipeline

st.set_page_config(
    page_title="StoryTone – AI Story to Music",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------
# THEME & STYLING
# ----------------------
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
        }
        .main-title {
            font-size: 48px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #b0b0b0;
            margin-bottom: 30px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            margin-top: 30px;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: #888888;
            margin-top: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# HEADER
# ----------------------
st.markdown("<div class='main-title'>🎼 StoryTone</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Turn stories into emotionally evolving soundtracks using AI</div>",
    unsafe_allow_html=True
)

# ----------------------
# INTRO
# ----------------------
st.markdown(
    """
    StoryTone is an AI-powered system that analyzes the emotional flow of a story and generates
    a dynamic background soundtrack that evolves with the narrative. It combines NLP-based
    emotion detection with custom audio synthesis to create expressive soundscapes.
    """
)

# ----------------------
# INPUT SECTION
# ----------------------
st.markdown("<div class='section-title'>📖 Your Story</div>", unsafe_allow_html=True)

story_text = st.text_area(
    "Paste your story below",
    height=260,
    placeholder="She was extremely happy to see him again after so many years. But soon, the room felt empty and silent..."
)

# ----------------------
# ACTION BUTTON
# ----------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_button = st.button("🎵 Generate Emotional Soundtrack", use_container_width=True)

# ----------------------
# PROCESSING
# ----------------------
if generate_button:
    if not story_text.strip():
        st.warning("Please enter a story before generating music.")
    else:
        status = st.empty()
        status.info("🔍 Analyzing emotions and composing music...")

        pipeline = StoryPipeline()
        output_file = pipeline.process_story(story_text)

        status.success("✅ Soundtrack generated successfully!")

        # ----------------------
        # OUTPUT SECTION
        # ----------------------
        st.markdown("<div class='section-title'>🎧 Generated Soundtrack</div>", unsafe_allow_html=True)
        st.audio(output_file)

        with open(output_file, "rb") as f:
            st.download_button(
                label="⬇️ Download Soundtrack",
                data=f,
                file_name="storytone_soundtrack.wav",
                mime="audio/wav",
                use_container_width=True
            )

# ----------------------
# FOOTER
# ----------------------
st.markdown(
    "<div class='footer'>Built as an end-to-end AI system combining NLP, signal processing, and creative coding</div>",
    unsafe_allow_html=True
)
