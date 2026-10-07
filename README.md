# Travel UGC Agent System

This project is a local-first creator workflow for building travel UGC reels from photos and stock footage, generating voiceovers using your own cloned voice, and turning attention into affiliate income and digital products.

It is designed for:
- iPhone Pro Max workflows
- Google Edge AI / Gemma local inference
- CapCut-style automation patterns
- reverse-funnel marketing logic
- private local memory and file-based agent workflows

## Features
- Photo + video reel assembly
- AI clip editing patterns similar to CapCut smart cuts
- iOS voice memo / Notes / WAV voice import
- local voice profile training
- AI voiceover generation from your own voice
- niche-first reverse funnel planning
- affiliate and travel payout tracking hooks
- landing-page generation ready for CTA conversion
- edge-AI export for local model usage

## Folder layout
- `src/video_generation/` — reel creation and smart editing
- `src/voice_clone/` — voice capture, training, synthesis
- `src/funnel_automation/` — reverse funnel logic
- `src/edge_ai_export/` — edge AI packaging
- `config/` — runtime config
- `docs/` — setup and workflow guides

## Quick use

### 1. Record voice sample
Use Voice Memos, Notes audio, or a WAV file and place it under `media/voice_samples/`.

### 2. Train your cloned voice
```bash
python -m src.voice_clone.voice_trainer --audio ./media/voice_samples/my_sample.wav --name my_travel_voice --style casual_storytelling
```

### 3. Build reel from photos and clips
```bash
python -m src.video_generation.photo_to_reel \
  --photos ./media/photos/p1.jpg ./media/photos/p2.jpg \
  --videos ./media/videos/clip1.mp4 ./media/videos/clip2.mp4 \
  --voice ./output/voiceovers/sample.mp3 \
  --output-dir ./output/reels \
  --title hidden_beach_reel
```

### 4. Apply smart edit
```bash
python -m src.video_generation.ai_video_editor --video ./output/reels/hidden_beach_reel.mp4 --style capcut_smart_cut
```

### 5. Export for Edge AI
```bash
python -m src.edge_ai_export.edge_ai_packager --name travel_ugc_agent --model gemma-2b-edge
```

## Notes
- This project is intentionally local-first and privacy-conscious.
- It does not require a cloud-only workflow.
- It is optimized for a creator who wants to publish fast without losing personal voice or control over assets.
