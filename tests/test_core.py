import io
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from src.script_engine.gemma_script_gen import ScriptGenerator
from src.video_generation.photo_to_reel import PhotoToReel
from src.funnel_automation.affiliate_mapper import AffiliateMapper
from src.voice_clone.voice_synthesizer import VoiceSynthesizer


class CoreTests(unittest.TestCase):
    def test_bilingual_generation(self):
        content = {lang: {k: "draft" for k in ("hook", "script", "caption", "cta")} for lang in ("en", "pt_br")}
        with tempfile.TemporaryDirectory() as tmp, patch("src.script_engine.gemma_script_gen.urlopen", return_value=io.BytesIO(json.dumps({"response": json.dumps(content)}).encode())):
            result = ScriptGenerator(output_dir=tmp).generate("London")
            self.assertEqual(result["status"], "draft_requires_review")
            self.assertEqual(len(list(Path(tmp).glob("*.json"))), 1)

    def test_empty_prompt(self):
        with self.assertRaises(ValueError):
            ScriptGenerator().generate(" ")

    def test_no_fake_affiliate(self):
        self.assertEqual(AffiliateMapper().map_offer("London")["status"], "no_verified_offer")

    def test_missing_media(self):
        with self.assertRaises(ValueError):
            PhotoToReel().create([])

    def test_unsafe_title(self):
        with self.assertRaises(ValueError):
            PhotoToReel().create([], title="../escape")

    def test_voice_requires_credentials(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                VoiceSynthesizer().generate("hello", {})
