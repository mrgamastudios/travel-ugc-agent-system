# Setup guide

## 1. Prepare your local media folder
Create these directories:
- `media/photos/`
- `media/videos/`
- `media/voice_samples/`
- `output/reels/`
- `output/voiceovers/`

## 2. Add your voice sample
Record a 30–60 second voice sample in:
- Voice Memos
- Notes audio recording
- WAV file from Files app

## 3. Train your voice profile
```bash
python -m src.voice_clone.voice_trainer --audio ./media/voice_samples/my_sample.wav --name my_travel_voice --style casual_storytelling
```

## 4. Build a reel from photos and stock clips
```bash
python -m src.video_generation.photo_to_reel \
  --photos ./media/photos/p1.jpg ./media/photos/p2.jpg \
  --videos ./media/videos/clip1.mp4 ./media/videos/clip2.mp4 \
  --voice ./output/voiceovers/my_voice_voiceover.mp3 \
  --output-dir ./output/reels \
  --title hidden_beach_reel
```

## 5. Apply smart edit
```bash
python -m src.video_generation.ai_video_editor --video ./output/reels/hidden_beach_reel.mp4 --style capcut_smart_cut
```

## 6. Export for edge AI usage
```bash
python -m src.edge_ai_export.edge_ai_packager --name travel_ugc_agent --model gemma-2b-edge
```

## Notes
- This workflow is local-first and privacy-minded.
- You can keep voice samples, route logic, scripts, and notes in your own files and memory folders.
