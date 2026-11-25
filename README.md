# Travel UGC Agent System — LairtonUK Creator OS

Local-first creator workflow for bilingual travel content and vertical video.

## Phase 1
See [setup and limitations](docs/CREATOR_OS.md) for the Mac dashboard, Ollama, FFmpeg, tests and optional cloud voice synthesis.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py --server.address 127.0.0.1
```

Install FFmpeg and start Ollama with the model described in the setup guide first. All drafts require manual review. No automatic social publishing or verified live affiliate integration is included. Legacy modules for smart editing, voice fingerprinting and edge export are prototypes.
