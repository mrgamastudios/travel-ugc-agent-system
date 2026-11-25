import argparse
import json
import os
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen
from uuid import uuid4


class VoiceSynthesizer:
    def __init__(self, output_dir="./output/voiceovers"):
        self.output_dir = Path(output_dir)

    def generate(self, script, voice_profile, output_format="mp3"):
        if output_format != "mp3":
            raise ValueError("Only MP3 is supported")
        voice_id = voice_profile.get("elevenlabs_voice_id")
        key = os.environ.get("ELEVENLABS_API_KEY")
        if not key or not voice_id:
            raise ValueError("Configure ELEVENLABS_API_KEY and a consented ElevenLabs voice ID; local fingerprints are not voice models")
        request = Request("https://api.elevenlabs.io/v1/text-to-speech/" + quote(voice_id, safe="") + "?output_format=mp3_44100_128",
            data=json.dumps({"text": script, "model_id": "eleven_multilingual_v2"}).encode(),
            headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        with urlopen(request, timeout=120) as response:
            if response.headers.get_content_type() != "audio/mpeg":
                raise ValueError("Provider did not return MP3")
            audio = response.read()
        if not audio:
            raise ValueError("Empty audio response")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        path = self.output_dir / (uuid4().hex + ".mp3")
        path.write_bytes(audio)
        return {"status": "generated_cloud_audio", "filepath": str(path)}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--script", required=True)
    p.add_argument("--voice-profile", required=True)
    p.add_argument("--format", default="mp3")
    a = p.parse_args()
    print(json.dumps(VoiceSynthesizer().generate(a.script, json.loads(Path(a.voice_profile).read_text()), a.format)))
