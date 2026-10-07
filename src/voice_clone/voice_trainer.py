import argparse
import hashlib
import json
from pathlib import Path


class VoiceTrainer:
    def __init__(self, output_dir="./data/voice_profiles"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def train(self, audio_path, name="my_voice", style="casual_storytelling"):
        audio = Path(audio_path)
        if not audio.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        audio_bytes = audio.read_bytes()
        voice_hash = hashlib.sha256(audio_bytes).hexdigest()[:16]
        profile = {
            "name": name,
            "style": style,
            "audio_path": str(audio),
            "voice_hash": voice_hash,
            "status": "trained_local",
            "compatible_formats": ["wav", "m4a", "mp3"],
            "voice_note": "Stateless local profile with no cloud upload"
        }

        output_path = self.output_dir / f"{name}.json"
        output_path.write_text(json.dumps(profile, indent=2), encoding="utf-8")
        return profile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a local voice profile from an audio sample")
    parser.add_argument("--audio", required=True, help="Path to WAV, M4A, or MP3 file")
    parser.add_argument("--name", default="my_voice")
    parser.add_argument("--style", default="casual_storytelling")
    args = parser.parse_args()

    profile = VoiceTrainer().train(args.audio, args.name, args.style)
    print(json.dumps(profile, indent=2))
