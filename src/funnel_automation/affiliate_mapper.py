import argparse
import json
from pathlib import Path


class AffiliateMapper:
    def __init__(self):
        self.networks = {
            "booking.com": {"commission_type": "percentage", "default_rate": "10%", "category": "hotels"},
            "expedia": {"commission_type": "percentage", "default_rate": "8%", "category": "travel"},
            "skyscanner": {"commission_type": "commission", "default_rate": "varies", "category": "flights"},
            "getyourguide": {"commission_type": "percentage", "default_rate": "5%", "category": "experiences"},
            "airbnb": {"commission_type": "referral", "default_rate": "varies", "category": "stays"},
        }

    def map_offer(self, destination, type_name="hotel"):
        return {
            "destination": destination,
            "type": type_name,
            "network": "booking.com",
            "recommended_link": "https://www.booking.com",
            "commission": self.networks["booking.com"]["default_rate"],
            "notes": "Best default affiliate fit for travel accommodation offers"
        }

    def track(self, affiliate_id, campaign_name, clicks=0, conversions=0):
        return {
            "affiliate_id": affiliate_id,
            "campaign_name": campaign_name,
            "clicks": clicks,
            "conversions": conversions,
            "roi": round((conversions / clicks) * 100, 2) if clicks else 0,
            "status": "tracking_ready"
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map a travel destination to an affiliate offer")
    parser.add_argument("--destination", default="Bali")
    parser.add_argument("--type", default="hotel")
    args = parser.parse_args()

    result = AffiliateMapper().map_offer(args.destination, args.type)
    print(json.dumps(result, indent=2))
