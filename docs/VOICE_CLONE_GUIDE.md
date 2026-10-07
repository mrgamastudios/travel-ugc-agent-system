# Voice Clone Guide

## Goal
Create a local voice profile from your own recordings so your travel reels and voiceovers sound like you.

## Best sources
- iPhone Voice Memos
- Notes audio recordings
- WAV files in Files app
- M4A / MP3 files

## Best practice
Use a clean, short sample of your normal voice. Aim for 30–60 seconds with little background noise.

## Train your voice locally
```bash
python -m src.voice_clone.voice_trainer --audio ./media/voice_samples/my_sample.wav --name my_travel_voice --style casual_storytelling
```

## Generate a local voiceover payload
```bash
python -m src.voice_clone.voice_synthesizer --script "This hidden beach is unreal. I can’t believe this place is this quiet." --voice-profile ./data/voice_profiles/my_travel_voice.json --format mp3
```

## Recommended styles
- `casual_storytelling` — best for UGC vlogs
- `professional` — best for guides or product reviews
- `energetic` — best for destination hype clips

## Privacy
- Keep all profiles local
- Avoid uploading unless it is explicitly your choice
- Store output in your own project folders for a privacy-friendly setup
