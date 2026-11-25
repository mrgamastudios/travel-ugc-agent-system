import json
import tempfile
from pathlib import Path
from uuid import uuid4
import streamlit as st
from src.script_engine.gemma_script_gen import ScriptGenerator
from src.video_generation.photo_to_reel import PhotoToReel

st.set_page_config(page_title="LairtonUK Creator OS", page_icon="🎬")
st.title("LairtonUK Creator OS")
st.caption("Local drafts • English + Português brasileiro • Nothing publishes automatically")
brand = st.selectbox("Brand", ["LairtonUK", "Lairton Gama", "A Manual of London"])
idea = st.text_area("Content idea")
if st.button("Generate bilingual draft", disabled=not idea.strip()):
    try:
        with st.spinner("Running local Ollama..."):
            st.session_state["draft"] = ScriptGenerator().generate(idea, niche=brand)
    except Exception as exc:
        st.error(f"Generation failed: {exc}")
if "draft" in st.session_state:
    draft = st.session_state["draft"]
    st.json(draft)
    st.download_button("Download draft", json.dumps(draft, ensure_ascii=False, indent=2), "draft.json")
st.subheader("Render vertical video")
media = st.file_uploader("Photos or clips", type=["jpg", "jpeg", "png", "mp4", "mov"], accept_multiple_files=True)
voice = st.file_uploader("Optional voiceover", type=["mp3", "wav", "m4a"])
duration = st.slider("Duration (seconds)", 5, 60, 25)
if st.button("Render draft video", disabled=not media):
    try:
        with tempfile.TemporaryDirectory() as tmp:
            photos, videos = [], []
            for i, item in enumerate(media):
                suffix = Path(item.name).suffix.lower()
                path = Path(tmp) / (str(i) + suffix)
                path.write_bytes(item.getvalue())
                (photos if suffix in {".jpg", ".jpeg", ".png"} else videos).append(path)
            audio = None
            if voice:
                audio = Path(tmp) / ("voice" + Path(voice.name).suffix.lower())
                audio.write_bytes(voice.getvalue())
            with st.spinner("Rendering with FFmpeg..."):
                result = PhotoToReel().create(photos, videos, audio, uuid4().hex, duration)
            st.session_state["rendered"] = result["output_file"]
    except Exception as exc:
        st.error(f"Rendering failed: {exc}")
if "rendered" in st.session_state:
    st.video(st.session_state["rendered"])
    st.download_button("Download reel", Path(st.session_state["rendered"]).read_bytes(), "reel.mp4", "video/mp4")
