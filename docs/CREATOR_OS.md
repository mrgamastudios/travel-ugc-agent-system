# Creator OS Phase 1

Local Mac setup (Python 3.10+):
1. Install Ollama and FFmpeg (e.g. brew install ffmpeg).
2. Start Ollama and run `ollama pull gemma3:4b`.
3. Run `python3 -m venv .venv`, then `source .venv/bin/activate`.
4. Run `pip install -r requirements.txt`.
5. Run `python -m unittest discover -s tests -v`.
6. Run `streamlit run app.py --server.address 127.0.0.1`.

The dashboard generates local bilingual drafts and renders vertical video, with optional existing narration. Review all claims and rights before publication. Generated content stays under ignored output directories. Never commit credentials or voice recordings. The environment example is documentation only; export variables in your shell.

Optional ElevenLabs synthesis sends script text to the provider and may incur costs. Set ELEVENLABS_API_KEY in the environment and use a profile containing elevenlabs_voice_id for a voice you have permission to use. The old voice trainer only fingerprints samples; it does not train a voice. The old smart editor, TikTok uploader and edge packager remain prototypes, not production services. Affiliate mapping accepts manually reviewed offers only; no live Awin verification or publishing is implemented. Canva and Shopify are future integrations. The dashboard is localhost-only; do not expose it directly to the internet.

Tests mock model inference; live Ollama, ElevenLabs and FFmpeg rendering require integration validation on your machine.
