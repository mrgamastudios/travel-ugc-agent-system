import argparse
import json
from pathlib import Path


class EdgeAIExporter:
    def __init__(self, output_dir="./output/edge_ai"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export(self, package_name="travel_ugc_agent", model_name="gemma-2b-edge"):
        bundle = {
            "name": package_name,
            "model": model_name,
            "generated_by": "travel-ugc-agent-system",
            "features": [
                "voice_clone",
                "reel_generation",
                "reverse_funnel",
                "landing_pages",
                "affiliate_tracking"
            ],
            "local_only": True
        }

        output_path = self.output_dir / f"{package_name}.json"
        output_path.write_text(json.dumps(bundle, indent=2), encoding="utf-8")
        return str(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package the project for local edge-AI export")
    parser.add_argument("--name", default="travel_ugc_agent")
    parser.add_argument("--model", default="gemma-2b-edge")
    args = parser.parse_args()

    result = EdgeAIExporter().export(args.name, args.model)
    print(json.dumps({"export_path": result}, indent=2))
