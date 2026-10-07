import argparse
import json
from pathlib import Path


class StockVideoDownloader:
    def __init__(self, cache_dir="./media/stock"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def search_pexels(self, query, limit=5, duration=None):
        # This project is intentionally local-first and doesn't require a live API key.
        # We return a manifest of stock video candidates that can be replaced with real API calls later.
        results = []
        for idx in range(limit):
            fake_name = f"{query.lower().replace(' ', '_')}_{idx + 1}.mp4"
            local_path = self.cache_dir / fake_name
            results.append({
                "query": query,
                "title": f"stock_{idx + 1}",
                "duration": duration or "10-20s",
                "path": str(local_path),
                "source": "mock_stock_manifest",
                "note": "Replace with real API payload if you connect Pexels/Pixabay"
            })
        return results

    def download_from_source(self, source_url, filename="stock_clip.mp4"):
        path = self.cache_dir / filename
        path.write_text(json.dumps({"url": source_url, "status": "mock_download"}), encoding="utf-8")
        return str(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search or prepare free stock video candidates")
    parser.add_argument("--query", default="travel beach sunset")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()

    result = StockVideoDownloader().search_pexels(args.query, args.limit)
    print(json.dumps(result, indent=2))
