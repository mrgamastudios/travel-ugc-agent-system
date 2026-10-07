import argparse
import json
from pathlib import Path


class VoiceRecorder:
    def __init__(self, input_dir="./media/voice_samples"):
        self.input_dir = Path(input_dir)
        self.input_dir.mkdir(parents=True, exist_ok=True)

    def import_from_file(self, filepath, name="voice_sample"):
        source = Path(filepath)
        if not source.exists():
            raise FileNotFoundError(f"Voice sample not found: {filepath}")

        destination = self.input_dir / f"{name}{source.suffix}"
        destination.write_bytes(source.read_bytes())
        return str(destination)

    def import_from_notes_or_memos(self, filepath, name="voice_sample"):
        return self.import_from_file(filepath, name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import a voice sample from iOS or a local WAV/M4A file")
    parser.add_argument("--filepath", required=True, help="Path to audio file")
    parser.add_argument("--name", default="voice_sample")
    args = parser.parse_args()

    result = VoiceRecorder().import_from_file(args.filepath, args.name)
    print(json.dumps({"imported": result}, indent=2))
