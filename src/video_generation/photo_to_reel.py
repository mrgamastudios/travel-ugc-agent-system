import argparse
import json
import shutil
import subprocess
from pathlib import Path


class PhotoToReel:
    def __init__(self, output_dir="./output/reels"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def create(self, photos, videos=None, voiceover=None, title="travel_reel", duration_seconds=25):
        videos = videos or []
        manifest = {
            "title": title,
            "photos": [str(p) for p in photos],
            "videos": [str(v) for v in videos],
            "voiceover": str(voiceover) if voiceover else None,
            "duration_seconds": duration_seconds,
            "aspect_ratio": "9:16",
            "format": "tiktok_reel",
            "status": "created_local_manifest"
        }

        output_file = self.output_dir / f"{title}.mp4"
        manifest["output_file"] = str(output_file)

        if shutil.which("ffmpeg") is not None:
            try:
                ffmpeg_cmd = ["ffmpeg", "-y"]
                for photo in photos:
                    ffmpeg_cmd.extend(["-loop", "1", "-t", "2", "-i", str(photo)])
                for video in videos:
                    ffmpeg_cmd.extend(["-i", str(video)])
                ffmpeg_cmd.extend(["-filter_complex", "concat=n=1:v=1:a=0", "-c:v", "libx264", "-pix_fmt", "yuv420p", str(output_file)])
                subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                manifest["status"] = "rendered_with_ffmpeg"
            except Exception:
                manifest["status"] = "manifest_only_fallback"

        manifest_file = self.output_dir / f"{title}_manifest.json"
        manifest_file.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a reel from selected photos and stock video assets")
    parser.add_argument("--photos", nargs="*", default=[], help="Photo file paths")
    parser.add_argument("--videos", nargs="*", default=[], help="Video file paths")
    parser.add_argument("--voice", default=None, help="Optional voiceover path")
    parser.add_argument("--title", default="travel_reel")
    parser.add_argument("--output-dir", default="./output/reels")
    parser.add_argument("--duration", type=int, default=25)
    args = parser.parse_args()

    result = PhotoToReel(args.output_dir).create(args.photos, args.videos, args.voice, args.title, args.duration)
    print(json.dumps(result, indent=2))
