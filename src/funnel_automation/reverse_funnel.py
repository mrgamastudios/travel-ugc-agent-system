import argparse
import json
from pathlib import Path


class ReverseFunnel:
    def __init__(self):
        self.steps = [
            "ugc_content",
            "niche_identification",
            "audience_segmentation",
            "offer_proposition",
            "conversion",
            "retargeting"
        ]

    def create(self, ugc_videos, niche, audience, offers):
        return {
            "ugc_videos": ugc_videos,
            "niche": niche,
            "audience": audience,
            "offers": offers,
            "steps": self.steps,
            "logic": "UGC first -> niche narrowed -> audience trusted -> digital product or affiliate offer"
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a reverse funnel from UGC to a monetized offer")
    parser.add_argument("--ugc", nargs="*", default=[], help="UGC videos or clips")
    parser.add_argument("--niche", default="budget_travel")
    parser.add_argument("--audience", default="travelers_18_35")
    parser.add_argument("--offer", action="append", default=["travel_guide", "affiliate_link"])
    args = parser.parse_args()

    result = ReverseFunnel().create(args.ugc, args.niche, args.audience, args.offer)
    print(json.dumps(result, indent=2))
