import argparse
import json
from pathlib import Path


class TikTokUploader:
    def __init__(self, output_dir="./output/publishing"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def post(self, video_path, caption, hashtags=None, schedule=None):
        payload = {
            "video_path": str(video_path),
            "caption": caption,
            "hashtags": hashtags or ["#TravelTok", "#TravelUGC", "#HiddenGems"],
            "schedule": schedule or "best_time_window",
            "platform": "TikTok",
            "status": "mock_publish_ready"
        }
        file_path = self.output_dir / "tiktok_publish.json"
        file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        return payload


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a mock TikTok publish payload")
    parser.add_argument("--video", default="./output/reels/travel_reel.mp4")
    parser.add_argument("--caption", default="Hidden gem travel reel")
    parser.add_argument("--hashtag", action="append", default=["#TravelTok", "#TravelUGC"])
    args = parser.parse_args()

    result = TikTokUploader().post(args.video, args.caption, args.hashtag)
    print(json.dumps(result, indent=2))
