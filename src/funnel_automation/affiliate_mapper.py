import argparse
import json
from urllib.parse import urlparse


class AffiliateMapper:
    def __init__(self, offers=None):
        self.offers = offers or []

    def map_offer(self, destination, type_name="hotel"):
        matches = [o for o in self.offers if o.get("category") == type_name
                   and o.get("approved") is True and o.get("verified_at")
                   and urlparse(o.get("tracking_url", "")).scheme == "https"
                   and urlparse(o.get("tracking_url", "")).hostname]
        return {"destination": destination, "type": type_name,
                "status": "requires_manual_offer_review" if matches else "no_verified_offer",
                "offers": matches}

    def track(self, affiliate_id, campaign_name, clicks=0, conversions=0):
        if min(clicks, conversions) < 0:
            raise ValueError("Counts must be nonnegative")
        return {"affiliate_id": affiliate_id, "campaign_name": campaign_name,
                "clicks": clicks, "conversions": conversions,
                "conversion_rate_percent": round(conversions / clicks * 100, 2) if clicks else 0}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--destination", required=True)
    p.add_argument("--type", default="hotel")
    a = p.parse_args()
    print(json.dumps(AffiliateMapper().map_offer(a.destination, a.type), indent=2))
