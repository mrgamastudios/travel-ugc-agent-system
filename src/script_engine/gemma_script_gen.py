import argparse
import json
from pathlib import Path


class ScriptGenerator:
    def __init__(self, model="gemma-2b-edge", output_dir="./output/scripts"):
        self.model = model
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, prompt, audience=None, niche=None, tone="casual_storytelling"):
        audience = audience or "travelers looking for hidden gems"
        niche = niche or "UK + global travel"

        hooks = [
            "POV: I found a place I never want to leave.",
            "This hidden gem is why I never book the obvious tourist spots.",
            "I wish someone told me about this before I booked my trip.",
            "The best part of this destination was not the obvious view...",
        ]

        body = (
            f"I was in {niche} and wanted to find something that felt more local than touristy. "
            f"I started with a simple idea: create a trip that felt personal, useful, and worth the money. "
            f"The result was a place that gave better value, better vibes, and better stories than the usual spots. "
            f"If you're building a travel plan, this is exactly the kind of place I would recommend to someone like {audience}."
        )

        script = {
            "model": self.model,
            "prompt": prompt,
            "audience": audience,
            "niche": niche,
            "tone": tone,
            "hook": hooks[0],
            "script": f"{hooks[0]}\n\n{body}\n\nSave this for your next trip and follow for more travel ideas.",
            "cta": "Save this for your next trip and comment 'GUIDE' for the itinerary."
        }

        output_file = self.output_dir / "generated_script.json"
        output_file.write_text(json.dumps(script, indent=2), encoding="utf-8")
        return script


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a travel script for UGC reels")
    parser.add_argument("--prompt", default="Hidden gem travel reel", help="User prompt")
    parser.add_argument("--audience", default="travelers looking for hidden gems")
    parser.add_argument("--niche", default="UK + global travel")
    parser.add_argument("--tone", default="casual_storytelling")
    args = parser.parse_args()

    result = ScriptGenerator().generate(args.prompt, args.audience, args.niche, args.tone)
    print(json.dumps(result, indent=2))
