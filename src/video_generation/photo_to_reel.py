import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory


class PhotoToReel:
    def __init__(self, output_dir="./output/reels"):
        self.output_dir = Path(output_dir)

    def create(self, photos, videos=None, voiceover=None, title="travel_reel", duration_seconds=25):
        if not re.fullmatch(r"[A-Za-z0-9_-]+", title):
            raise ValueError("Title must contain only letters, digits, underscores or hyphens")
        assets = [(Path(p), True) for p in photos] + [(Path(v), False) for v in (videos or [])]
        if not assets or duration_seconds <= 0:
            raise ValueError("Provide media and a positive duration")
        for path in [p for p, _ in assets] + ([Path(voiceover)] if voiceover else []):
            if not path.is_file():
                raise FileNotFoundError(path)
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            raise RuntimeError("Install FFmpeg before rendering")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        output = self.output_dir / (title + ".mp4")
        segment_duration = duration_seconds / len(assets)
        def run(args):
            subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-nostdin", "-y", *args], check=True, capture_output=True)
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            for i, (path, photo) in enumerate(assets):
                source = ["-loop", "1"] if photo else ["-stream_loop", "-1"]
                run(source + ["-i", str(path.resolve()), "-t", str(segment_duration),
                    "-vf", "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30",
                    "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(root / f"clip{i}.mp4")])
            listing = root / "clips.txt"
            listing.write_text("".join(f"file 'clip{i}.mp4'\n" for i in range(len(assets))))
            args = ["-f", "concat", "-safe", "1", "-i", str(listing)]
            if voiceover:
                args += ["-i", str(Path(voiceover).resolve()), "-map", "0:v:0", "-map", "1:a:0", "-af", "apad", "-c:a", "aac"]
            else:
                args += ["-map", "0:v:0", "-an"]
            rendered = root / "rendered.mp4"
            run(args + ["-c:v", "copy", "-t", str(duration_seconds), "-movflags", "+faststart", str(rendered)])
            shutil.copyfile(rendered, output)
        manifest = {"title": title, "output_file": str(output), "status": "rendered_with_ffmpeg", "aspect_ratio": "9:16"}
        (self.output_dir / (title + "_manifest.json")).write_text(json.dumps(manifest, indent=2))
        return manifest


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--photos", nargs="*", default=[])
    p.add_argument("--videos", nargs="*", default=[])
    p.add_argument("--voice")
    p.add_argument("--title", default="travel_reel")
    p.add_argument("--output-dir", default="./output/reels")
    p.add_argument("--duration", type=int, default=25)
    a = p.parse_args()
    print(json.dumps(PhotoToReel(a.output_dir).create(a.photos, a.videos, a.voice, a.title, a.duration)))
