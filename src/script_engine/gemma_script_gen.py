import argparse
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from uuid import uuid4


class ScriptGenerator:
    def __init__(self, model=None, output_dir="./output/scripts"):
        self.model = model or os.environ.get("OLLAMA_MODEL", "gemma3:4b")
        self.output_dir = Path(output_dir)

    def generate(self, prompt, audience=None, niche=None, tone="casual_storytelling"):
        if not prompt.strip():
            raise ValueError("Enter a content idea")
        instruction = {
            "idea": prompt, "audience": audience or "UK travel audience",
            "niche": niche or "UK travel", "tone": tone
        }
        request = Request("http://127.0.0.1:11434/api/generate",
            data=json.dumps({"model": self.model, "stream": False, "format": "json",
                "prompt": "Write a draft travel short video in English and Brazilian Portuguese. "
                "Return JSON with en and pt_br objects, each containing hook, script, caption and cta strings. "
                "Do not invent prices, dates, personal experiences or verified facts. Mark uncertain claims for review. Brief: "
                + json.dumps(instruction)}).encode(),
            headers={"Content-Type": "application/json"})
        with urlopen(request, timeout=180) as response:
            result = json.loads(json.load(response)["response"])
        for lang in ("en", "pt_br"):
            if not isinstance(result.get(lang), dict) or not all(
                isinstance(result[lang].get(k), str) and result[lang][k].strip()
                for k in ("hook", "script", "caption", "cta")):
                raise ValueError("Model returned incomplete bilingual content")
        result["status"] = "draft_requires_review"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        path = self.output_dir / (uuid4().hex + ".json")
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--audience")
    parser.add_argument("--niche")
    parser.add_argument("--tone", default="casual_storytelling")
    args = parser.parse_args()
    print(json.dumps(ScriptGenerator().generate(args.prompt, args.audience, args.niche, args.tone), ensure_ascii=False, indent=2))
