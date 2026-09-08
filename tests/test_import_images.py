import base64
import tempfile
import unittest
from pathlib import Path

from tools.import_images import NAME, image_info, sha256


PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


class ImportImageTests(unittest.TestCase):
    def test_reads_real_png_signature_dimensions_and_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AQ-EX-001__v001.png"
            path.write_bytes(PNG_1X1)
            self.assertEqual(("png", 1, 1), image_info(path))
            self.assertEqual(64, len(sha256(path)))

    def test_rejects_ambiguous_browser_filename(self):
        self.assertIsNone(NAME.fullmatch("AQ-EX-001__v001 (1).png"))

    def test_accepts_canonical_filename(self):
        self.assertIsNotNone(NAME.fullmatch("AQ-MAG-021__v001.png"))


if __name__ == "__main__":
    unittest.main()
