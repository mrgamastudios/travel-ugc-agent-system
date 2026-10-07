import argparse
import json
from pathlib import Path


class LandingPageGen:
    def __init__(self, output_dir="./output/landing_pages"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, title, subtitle, cta_text, affiliate_link, hero_image=None):
        html = f"""
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{title}</title>
  <style>
    body {{
      margin: 0; font-family: Arial, sans-serif; background: #f6f2eb; color: #121212;
    }}
    .container {{ max-width: 1100px; margin: 0 auto; padding: 40px 20px 80px; }}
    .hero {{
      display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 30px; align-items: center;
      background: linear-gradient(135deg, #111827, #0f172a); color: white; border-radius: 28px; padding: 42px;
      box-shadow: 0 18px 45px rgba(0,0,0,0.12);
    }}
    .eyebrow {{ text-transform: uppercase; letter-spacing: 0.14em; font-size: 12px; opacity: 0.8; }}
    h1 {{ font-size: clamp(2.5rem, 5vw, 4.2rem); margin: 14px 0; line-height: 1.04; }}
    p {{ font-size: 1.05rem; line-height: 1.75; opacity: 0.94; }}
    .cta {{
      background: #fbbf24; color: #111827; border: none; padding: 18px 28px; border-radius: 999px;
      font-weight: 700; font-size: 1rem; cursor: pointer; text-decoration: none; display: inline-block; margin-top: 10px;
    }}
    .card {{ background: white; border-radius: 18px; padding: 22px; margin-top: 22px; box-shadow: 0 12px 30px rgba(0,0,0,0.06); }}
    .grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 30px; }}
    .feature {{ background: white; border-radius: 18px; padding: 22px; }}
    .feature h3 {{ margin-top: 0; }}
    .image-box {{
      min-height: 350px; background: linear-gradient(135deg, #f5d0fe, #dbeafe); border-radius: 24px;
      display:flex; align-items:center; justify-content:center; color:#0f172a; font-size: 1.2rem; font-weight: 700;
    }}
    @media (max-width: 760px) {{
      .hero, .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class=\"container\">
    <div class=\"hero\">
      <div>
        <div class=\"eyebrow\">Travel UGC Funnel</div>
        <h1>{title}</h1>
        <p>{subtitle}</p>
        <a class=\"cta\" href=\"{affiliate_link}\">{cta_text}</a>
      </div>
      <div class=\"image-box\">{hero_image or 'Hidden gem + itinerary + value'}</div>
    </div>

    <div class=\"grid\">
      <div class=\"feature\">
        <h3>Why this works</h3>
        <p>Authentic UGC creates trust before the offer, which makes the CTA feel more useful and less salesy.</p>
      </div>
      <div class=\"feature\">
        <h3>What you get</h3>
        <p>Top places, itinerary notes, best travel hacks, and destination-specific booking suggestions.</p>
      </div>
      <div class=\"feature\">
        <h3>Monetization</h3>
        <p>Affiliate booking links, offer-based content, and guide upsells tied to real travel trust.</p>
      </div>
    </div>

    <div class=\"card\">
      <h2>Travel smarter</h2>
      <p>Use the destination strategy from this video, pair it with your itinerary, and save time by going directly to the best-value booking options.</p>
      <a class=\"cta\" href=\"{affiliate_link}\">{cta_text}</a>
    </div>
  </div>
</body>
</html>
"""
        output_file = self.output_dir / f"{title.lower().replace(' ', '_')}.html"
        output_file.write_text(html, encoding="utf-8")
        return str(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a hyper-frame style landing page")
    parser.add_argument("--title", default="Hidden Gem Travel Guide")
    parser.add_argument("--subtitle", default="A destination plan built around what actually matters: value, experience, and atmosphere.")
    parser.add_argument("--cta", default="Book this trip")
    parser.add_argument("--affiliate-link", default="https://www.booking.com")
    args = parser.parse_args()

    output = LandingPageGen().generate(args.title, args.subtitle, args.cta, args.affiliate_link)
    print(json.dumps({"landing_page": output}, indent=2))
